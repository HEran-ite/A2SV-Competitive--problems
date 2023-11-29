class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        kel=float(celsius+273.15)
        fah=float(celsius*1.80+32.00)
        return[kel,fah]
