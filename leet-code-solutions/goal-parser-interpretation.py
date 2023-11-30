class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        res= command.replace('G','G')
        res= res.replace('()','o')
        res= res.replace('(al)','al')
        return (res)
            