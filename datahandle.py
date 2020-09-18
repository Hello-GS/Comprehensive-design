import os
import cv2
import matplotlib.pyplot as plt
def read_file(filename):
    q =0 
    count0 = {}
    count1 = {}
    dir0 = {}
    dir1 = {}
    dir0_event = {}
    dir1_event = {}

    with open(filename) as txtdata:
        lines = txtdata.readlines()
        for line in lines:

            str_lable = line.strip().split('  ')
            txt = '/Users/gaoshang/PycharmProjects/LAB/test.txt'
            test = open(txt, 'a')

            if str_lable[1] == '0':
                q+=1
                str_list = str_lable[0].split('.')
                event = str_list[2]
                year = str_list[3][0:4]
                if year in count0.keys():
                    count0[year] += 1
                else:
                    count0[year] = 1
                if event in dir0_event.keys():
                    dir0_event[event]+=1
                else:
                    dir0_event[event] = 1
                if year in dir0.keys():
                    if event not in dir0[year]:
                        dir0[year].append(event)
                    else:
                        continue
                else:
                    list = []
                    list.append(event)
                    dir0[year]=list
            else:
                
                str_list = str_lable[0].split('.')
                event = str_list[2]
                year = str_list[3][0:4]
                if year in count1.keys():
                    count1[year] += 1
                else:
                    count1[year] = 1
                if event in dir1_event.keys():
                    dir1_event[event]+=1
                else:
                    dir1_event[event] = 1
                if year in dir1.keys():
                    if event not in dir1[year]:
                        dir1[year].append(event)
                    else:
                        continue
                else:
                    list = []
                    list.append(event)
                    dir1[year] = list
        # for i in dir0_event.keys():
        #     print(i+" "+ str(dir0_event[i]))
        # print(".......")
        # for i in dir0.keys():
        #     print( str(i)+" "+ str(len(dir0[i])))
        # print(".......")
        # for i in dir1_event.keys():
        #     print(i+" "+ str(dir1_event[i]))
        # print(".......")
        # for j in dir1.keys():
        #     print(j+" "+ str(len(dir1[j])))
        list0_year = []
        list0_event = []
        list0_year_count = []
        list0_event_count = []
        list1_year = []
        list1_event = []
        list1_year_count = []
        list1_event_count = []

        year_label0 = []
        label0_count = []
        year_label1 = []
        label1_count = []

        

        for i in dir0.keys():
            list0_year.append(int(i))
            list0_year_count.append(len(dir0[i]))
        for i in dir1.keys():
            list1_year.append(int(i))
            list1_year_count.append(len(dir1[i]))
        for i in dir0_event.keys():
            list0_event.append(int(i))
            list0_event_count.append(int(dir0_event[i]))
        for i in dir1_event.keys():
            list1_event.append(int(i))
            list1_event_count.append(int(dir1_event[i]))

        for i in count0.keys():
            year_label0.append(int(i))
            label0_count.append(count0[i])
        for i in count1.keys():
            year_label1.append(int(i))
            label1_count.append(count1[i])


        
        
        Interval0 = []
        num0=[]
        Interval0_count = {'0-20': 0, '20-40':0, '40-60':0, '60-80':0, '80-100':0, '>100':0}
        Interval1 =[]
        num1=[]
        Interval1_count = {'0-20': 0, '20-40':0, '40-60':0, '60-80':0, '80-100':0, '>100':0}
        for i in list0_event_count:
            if i>=0 and i<20:
                Interval0_count['0-20']+=1
            elif i>=20 and i<40:
                Interval0_count['20-40']+=1
            elif i>=40 and i<60:
                Interval0_count['40-60']+=1
            elif i>=60 and i<80:
                Interval0_count['60-80']+=1
            elif i>=80 and i<100:
                Interval0_count['80-100']+=1
            else:
                Interval0_count['>100']+=1

        
        for i in list1_event_count:
            if i>=0 and i<20:
                Interval1_count['0-20']+=1
            elif i>=20 and i<40:
                Interval1_count['20-40']+=1
            elif i>=40 and i<60:
                Interval1_count['40-60']+=1
            elif i>=60 and i<80:
                Interval1_count['60-80']+=1
            elif i>=80 and i<100:
                Interval1_count['80-100']+=1
            else:
                Interval1_count['>100']+=1
        

        s=0
        for i in list0_event_count:
            s+=i
        print(s,q)
        for i in Interval0_count.keys():
            Interval0.append(i)
            num0.append(Interval0_count[i])

        
        for i in Interval1_count.keys():
            Interval1.append(i)
            num1.append(Interval1_count[i])
            

        

        




        # plt.bar(list0_year ,list0_year_count, label='label0')
        # plt.bar(list1_year, list1_year_count, label='label1')
        # plt.xlabel('Year')
        # plt.ylabel('event_count')
        # plt.legend()

        # plt.bar(year_label0, label0_count, label='label0')
        # plt.bar(year_label1, label1_count, label='label1')
        # plt.xlabel('Year')
        # plt.ylabel('photo_count')
        # plt.legend()


        plt.bar(list0_event, list0_event_count, width = 15,label='label0')
        plt.bar(list1_event, list1_event_count, width = 15, label='label1')
        
        plt.xlabel('event')
        plt.ylabel('photo_count')
        plt.legend()



        # plt.bar(Interval0, num0, label='label0')
        # plt.bar(Interval1, num1, label='label1')
        # plt.xlabel('Interval')
        # plt.ylabel('event_count')
        # plt.legend()

        

        #ax2.bar(list0_event, list0_event_count, label='label0')
        #ax2.hist(list0_event, list0_event_count, histtype='bar', rwidth=0.8)
        # ax2.hist(list1_event, list1_event_count, histtype='bar', rwidth=0.8)
        #ax2.bar(list1_event, list1_event_count, label='label1')
        #ax2.legend()
        #plt.hist(salary, group, histtype='bar', rwidth=0.8)
        plt.show()






read_file('/Users/gaoshang/PycharmProjects/LAB/alldata_output.txt')
