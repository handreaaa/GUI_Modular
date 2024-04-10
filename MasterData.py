class DataMaster():
    def __init__(self):
        
        self.SynchChannel = 0
        self.channels = 0
        self.msg = 0
        self.XData = []
        self.YData = []

    def DecodeMsg(self):
        temp = self.RowMsg.decode('ascii').strip().split(',')
        temp= [s for s in temp if s.strip()]
        self.channels = len(temp)
        self.msg = temp
        
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