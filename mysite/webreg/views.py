from django.shortcuts import render
import xlrd

from pymongo import MongoClient


def index(request):
    context = {
        "data": { "1":['ENG101', 256565, 3, 'Mr.Bob', 'Online', 'Open', 'Mondays @ 2'], "2":['ENG202', 256900, 2, 'Mr.Jones', 'Online', 'Open', 'Tuesdays @ 2']  },
        #"data": ['ENG101', 256565, 3, 'Mr.Bob', 'Online', 'Open', 'Mondays @ 2'],
        "x": ['1','2','3','4','5','6','7','8','9'],
        "cart" : { "1":['ENG101', 256565, 3, 'Mr.Bob', 'Online', 'Open', 'Mondays @ 2'], },
        "message" : [""]
    }
    context2 = {
        "data": { "first":['ENG101', 256565, 3, 'Mr.Bob', 'Online', 'Open', 'Mondays @ 2'],   },
        #"data": ['ENG101', 256565, 3, 'Mr.Bob', 'Online', 'Open', 'Mondays @ 2'],
        "x": [1,2],

    }
    context["cart"]= {}

    loc = ("webreg/courseinfo.xlsx")
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)
    for i in range(0,sheet.nrows):
        if(i==0):
            continue
        context["data"].update({ i : sheet.row_values(i)})
    del context['data']['1']
    del context['data']['2']
    #print(context)

    numofclasses = 1;
    if request.method == 'POST':
        for key,y in request.POST.items():
            if key == "csrfmiddlewaretoken":
                continue
            elif key == "registerclass":
                #DO IF CART HAS A 2, THEN PRINT THE MESSAGE
                if(context["cart"]):
                    if(context["cart"][1][0]=="ELEMENTARY ARABIC I"):
                        context["message"] = "*** ERROR "
                else:
                    context['temp'] = [context["data"][1][2], context["data"][1][10], context["data"][1][4]]
                    context["registered"] = {numofclasses: context["temp"]}
                    print(context["registered"])
            else:
                if(numofclasses==2):
                    context['temp']=[context["data"][2][2],context["data"][2][10], context["data"][2][4]]
                    context["cart"].update({ numofclasses : context["temp"]})

                context['temp'] = [context["data"][int(key)][2], context["data"][int(key)][10],context["data"][int(key)][4]]
                context["cart"].update({numofclasses: context["temp"]})
                numofclasses = numofclasses + 1
                print(context["cart"])
                print(numofclasses)


    # return response
    return render(request,'webreg/regpage.html',context)