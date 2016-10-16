def malloc(root_val):
    return UtilClass(root_val)

class UtilClass(object):
    def __init__(self, root_val):
        self.theRootObject = root_val

    def className(self):
        return "UtilClass"

    def rootObject(self):
        return self.theRootObject

    def utilLogit(str12, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if  str3 == "":
            logger.error(str12)
            return
        if  str4 == "":
            logger.error(str12, str3)
            return
        if  str5 == "":
            logger.error(str12, str3, str4)
            return
        if  str6 == "":
            logger.error(str12, str3, str4, str5)
            return
        if  str7 == "":
            logger.error(str12, str3, str4, str5, str6)
            return
        if  str8 == "":
            logger.error(str12, str3, str4, str5, str6, str7)
            return
        if  str9 == "":
            logger.error(str12, str3, str4, str5, str6, str7, str8)
            return
        if  str10 == "":
            logger.error(str12, str3, str4, str5, str6, str7, str8, str9)
            return
        if  str11 == "":
            logger.error(str12, str3, str4, str5, str6, str7, str8, str9, str10)
            return
        logger.error(str12, str3, str4, str5, str6, str7, str8, str9, str10, str11)


    def utilAbend(str12, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        utilLogit("Abend " + str12, str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)



import logging

logger = logging.getLogger(__name__)

def utilLogit(str12, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
    if  str3 == "":
        logger.error(str12)
        return
    if  str4 == "":
        logger.error(str12, str3)
        return
    if  str5 == "":
        logger.error(str12, str3, str4)
        return
    if  str6 == "":
        logger.error(str12, str3, str4, str5)
        return
    if  str7 == "":
        logger.error(str12, str3, str4, str5, str6)
        return
    if  str8 == "":
        logger.error(str12, str3, str4, str5, str6, str7)
        return
    if  str9 == "":
        logger.error(str12, str3, str4, str5, str6, str7, str8)
        return
    if  str10 == "":
        logger.error(str12, str3, str4, str5, str6, str7, str8, str9)
        return
    if  str11 == "":
        logger.error(str12, str3, str4, str5, str6, str7, str8, str9, str10)
        return
    logger.error(str12, str3, str4, str5, str6, str7, str8, str9, str10, str11)


def utilAbend(str12, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
    utilLogit("Abend " + str12, str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)
