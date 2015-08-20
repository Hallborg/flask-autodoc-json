def generate():
    objs = AUTO.generate()
    returnList = []
    for obj in objs:
        obj['methods'] = splitString(str(obj['methods']))
        returnList.append(obj)
    return Response(returnList, 200)


def splitString(methodString):
    methodList = []
    temp = methodString.replace('set([', '')
    tempList = temp.split(',')
    for idx, item in enumerate(tempList):
        if idx == len(tempList) - 1:
            item = item.replace('])', '')
        item = item.replace("'", "")
        item = item.replace(' ', '')
        methodList.append(item)
    return methodList

def testing_travis(a,b,c):
    return 'hello'
