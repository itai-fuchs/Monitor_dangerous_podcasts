class Text_analysis:

    def __init__(self,text,hostile_list,les_hostile_list):

        self.text=text
        self.hostile_list=hostile_list
        self.les_hostile_list=les_hostile_list

    def classification(self):
        rank = 0

        for word in self.hostile_list:
            if word in self.text:
                rank += 2

        for word in self.les_hostile_list:
            if word in self.text:
                rank += 1

        return rank

    def risk_percent(self):
        risk_percent=len(self.text.split())/self.classification()
        print(len(self.text.split()))
        return {"bds_percent":risk_percent}


    def criminal_event(self):
        risk_percent=self.risk_percent().val
        return {"is_bds":risk_percent > 75}

    # def risk_level(self):
    #     {"bds_threat_level":}
    #     pass