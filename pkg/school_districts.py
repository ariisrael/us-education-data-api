from utils import Url, getPaginatedResults

def url():
    return Url().topic('school-districts')

class CCD:
    @staticmethod
    def url():
        return url().source('ccd')

    @staticmethod
    def directory(year, filters={}):
        if not year:
            return False
        url = CCD.url().endpoint('directory').year(year).filters(filters)
        return getPaginatedResults(url)

    @staticmethod
    def enrollment(year, grade, disaggregations=[], filters={}):
        if not year or not grade:
            return False
        url = CCD.url().endpoint('enrollment').year(year).grade(grade).disaggregations(disaggregations).filters(filters)
        return getPaginatedResults(url)

    @staticmethod
    def finance(year, filters={}):
        if not year:
            return False
        url = CCD.url().endpoint('finance').year(year).filters(filters)
        return getPaginatedResults(url)

class SAIPE:
    @staticmethod
    def url():
        return url().source('saipe')

    @staticmethod
    def poverty_estimates(year, filters={}):
        if not year:
            return
        url = SAIPE.url().year(year).filters(filters)
        return getPaginatedResults(url)

class EDFacts: 
    @staticmethod
    def url():
        return url().source('edfacts')

    @staticmethod
    def state_assessments(year, grade, disaggregations=[], filters={}):
        if not year or not grade:
            return False
        url = EDFacts.url().endpoint('assessments').year(year).grade(grade).disaggregations(disaggregations).filters(filters)
        return getPaginatedResults(url)