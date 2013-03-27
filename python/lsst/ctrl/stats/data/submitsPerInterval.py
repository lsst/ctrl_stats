class SubmitsPerInterval:

    def __init__(self, dbm):
        self.dbm = dbm

    def calculate(self):
        query = 'select submitTime, count(*) as count from submissions group by submitTime;'
    
        results = dbm.execCommandN(query)
    
        values = []
        for res in results:
            submitTime = res[0]
            count = res[1]
            values.append([submitTime,count])
        return values