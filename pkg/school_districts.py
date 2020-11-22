from config import url
from utils import getPaginatedResults

url = url.format(topic='school-districts')
path = '/{source}/{endpoint}/{year}'

class CCD:
    source = 'ccd'

    @staticmethod
    def directory(year):
        endpoint = 'directory'
        if not year:
            return False
        directory_url = url + path.format(source=CCD.source, endpoint=endpoint, year=year)
        results = getPaginatedResults(directory_url)
        return results

    @staticmethod
    def enrollment(year, grade, disaggregations=[], filters={}):
        endpoint = 'enrollment'
        if not year or not grade:
            return False
        enrollment_path = path.format(source=CCD.source, endpoint=endpoint, year=year) + '/grade-{grade}'
        enrollment_url = url + enrollment_path.format(grade=grade)
        if disaggregations:
            if 'race' in disaggregations:
                enrollment_url += '/race'
            if 'sex' in disaggregations:
                enrollment_url += '/sex'
        if filters: 
            enrollment_url += '?'
            for key, value in filters.items():
                enrollment_url += key + '=' + str(value) + '&'
        results = getPaginatedResults(enrollment_url)
        return results

    @staticmethod
    def finance(year, filters={}):
        endpoint = 'finance'
        if not year:
            return False
        finance_url = url + path.format(source=CCD.source, endpoint=endpoint, year=year)
        if filters: 
            finance_url += '?'
            for key, value in filters.items():
                finance_url += key + '=' + str(value) + '&'
        results = getPaginatedResults(finance_url)
        return results

class SAIPE:

    @staticmethod
    def poverty_estimates(year, filters={}):
        if not year:
            return
        saipe_url = url + '/saipe/' + year
        if filters:
            saipe_url += '?'
            for key, value in filters.items():
                saipe_url += key + '=' + str(value) + '&'
        results = getPaginatedResults(saipe_url)
        return results

class EDFacts: 
    source = 'edfacts'

    @staticmethod
    def state_assessments(year, grade, disaggregations=[], filters={}):
        endpoint = 'assessments'
        if not year or not grade:
            return False
        assessments_path = path.format(source=EDFacts.source, endpoint=endpoint, year=year) + '/grade-{grade}'
        assessments_url = url + assessments_path.format(grade=grade)
        if disaggregations:
            if 'race' in disaggregations:
                assessments_url += '/race'
            if 'sex' in disaggregations:
                assessments_url += '/sex'
            if 'special-populations' in disaggregations:
                assessments_url += '/special-populations'
        if filters: 
            assessments_url += '?'
            for key, value in filters.items():
                assessments_url += key + '=' + str(value) + '&'
        results = getPaginatedResults(assessments_url)
        return results