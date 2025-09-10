class TextAnalysis:

    def __init__(self,text,hostile_list,les_hostile_list):

        self.text=text
        self.hostile_list=hostile_list
        self.les_hostile_list=les_hostile_list

    #Calculates amount of dangerous words in the text from words lists
    def dangerous_words(self):
        rank = 0

        for word in self.hostile_list:
            if word in self.text:
                rank += 2

        for word in self.les_hostile_list:
            if word in self.text:
                rank += 1

        return rank

    #Calculating risk percentages and normalize result
    def risk_percent(self):
        if self.dangerous_words() == 0:
            risk_percent= 0.0
        else:
            risk_percent= round((self.dangerous_words() / len(self.text.split()))*420, 2)
        return {"bds_percent":risk_percent}

    # Calculating if is criminal_event
    def criminal_event(self):
        risk_percent=self.risk_percent()["bds_percent"]
        return {"is_bds":risk_percent > 65}

    # Calculating the risk level
    def risk_level(self):
        threat_level="None"
        risk_percent = self.risk_percent()["bds_percent"]
        if risk_percent >=33 and risk_percent<66:
            threat_level = "medium"
        elif risk_percent >= 66:
            threat_level = "high"
        elif risk_percent>1 and risk_percent<33:
            threat_level = "low"


        return {"bds_threat_level":threat_level}
