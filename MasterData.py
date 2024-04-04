class DataMaster():
    def __init__(self):
        
        self.SynchChannel = 0

        self.msg = 0

        self.XData = []
        self.YData = []

    def DecodeMsg(self):
        temp = self.RowMsg.decode('ascii').strip().split(',')
        a1= [int(s) for s in temp]
        self.msg = a1[0]  
        '''
        if len(temp) > 0:
            if "#" in temp:
                self.msg = temp.split("#")
                # print(f"Before removing index :{self.msg}")
                del self.msg[0]
                # print(f"After removing index :{self.msg}")
        '''

    def GenChannels(self):
        self.Channels = [f"Ch{ch}" for ch in range(self.SynchChannel)]

    def buildYdata(self):
        for _ in range(self.SynchChannel):
            self.YData.append([])

    def ClearData(self):
        self.RowMsg = ""
        self.msg = 0
        self.Ydata = []