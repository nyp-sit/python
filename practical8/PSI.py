psiList = [{'region':'east', 'date': '16 Jul 2005', 'psi': '375'},
             {'region':'south', 'date': '21 Jun 2013', 'psi': '401'},
             {'region':'west', 'date': '25 Sep 2015', 'psi': '341'},
             {'region':'north', 'date': '3 Jun 2013', 'psi': '392'}]

region = ['north', 'south', 'east', 'west']

while True:
    print('PSI Application')
    print('1. To enter daily PSI reading for 4 regions in Singapore')
    print('2. To display the highest PSI reading')
    print('3. To display the lowest PSI reading')
    print('4. To display all PSI reading')
    print('Press any other numbers to exit')

    choice = int(input('Enter your option:'))

    if choice == 1:
        day = input('Enter the date of the PSI reading: ')
        for i in range (4):
            psi = int(input('Enter the psi reading for ' + region[i] + ":"))
            for aDict in psiList:
                if aDict["region"] == region[i] and psi > int(aDict['psi']):
                   aDict['psi']=psi
                   aDict['date'] = day

    elif choice == 2:
        max = 0
        for aDict in psiList:
            if int(aDict['psi']) > max:
                max = int(aDict['psi'])
        print('The highest PSI is', max)
    elif choice == 3:
        dic = psiList[0]
        min = int(dic['psi'])
        for aDict in psiList:
            if int(aDict['psi']) < min:
                min = int(aDict['psi'])
        print('The lowest PSI is', min)
    elif choice == 4:
        for aDict in psiList:
            print('Region:', aDict['region'], 'Date: ', aDict['date'], 'PSI: ', aDict['psi'])
    else:
        break
