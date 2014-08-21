#Creating weightloss class holding the attributes
class WeightLossTracker(object)
    def __init__(self)
        self.week1 = 0
        self.week2 = 0
        self.week3 = 0
        self.week4 = 0
        self.__total_weightloss = 0 #private attribute
        self.__avg_weighloss_week = 0 #private attribute
    

    # __total_weightloss getter
    @property
    def total_weightloss(self)
        self.__total_weightloss = self.week1 + self.week2 + self.week3 + self.week4
        return self.__total_weightloss
    
    # __total_weightloss setter
    @total_weightloss.setter
    def total_weightloss(self, new_total_weightloss)
        self.total_weightloss = new_total_weightloss
    
    # __avg_weighloss_week getter
    @property
    def avg_weighloss_week(self)
        self.__avg_weighloss_week = (self.week1 + self.week2 + self.week3 + self.week4)/4
        return self.__avg_weighloss_week
    
    # __total_weightloss setter
    @avg_weighloss_week.setter
    def avg_weighloss_week(self, new_avg_weighloss_week)
        self.avg_weighloss_week = new_avg_weighloss_week