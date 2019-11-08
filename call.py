class CallDetail:
    def __init__(self,call,recv,dur,typ):
        self.caller_no=call
        self.receiver_no=recv
        self.duration=dur
        self.type_of_call=typ

    def print_details(self):
        print("Call Details :\nCaller no. : ",self.caller_no,"\nReceiver no. : ",self.receiver_no,"\nDuration : ",self.duration," min\nType of Call : ",self.type_of_call,"\n")

class Util:
    
    def __init__(self):
        self.list_of_call_objects=[]

    def parse_customer(self,list_of_call_string):
        for i in list_of_call_string:
            call=i.split(',')
            self.list_of_call_objects.append(CallDetail(call[0],call[1],call[2],call[3]))

    def print_list(self):
        for call in self.list_of_call_objects:
            call.print_details()
            
call='9990000001,9330000001,23,STD'
call2='9990000004,9330000002,54,Local'
call3='9990000005,9330000003,6,ISD'
list_of_call_string=[call,call2,call3]
obj=Util()
obj.parse_customer(list_of_call_string) 
obj.print_list()
