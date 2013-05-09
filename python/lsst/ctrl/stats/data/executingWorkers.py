# 
# LSST Data Management System
# Copyright 2008-2013 LSST Corporation.
# 
# This product includes software developed by the
# LSST Project (http://www.lsst.org/).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the LSST License Statement and 
# the GNU General Public License along with this program.  If not, 
# see <http://www.lsstcorp.org/LegalNotices/>.
#
from lsst.ctrl.stats.data.dbEntry import DbEntry

class ExecutingWorkers:

    def __init__(self, dbm):
        self.dbm = dbm
        self.firstExecutingWorker = self.getFirst()
        self.lastExecutingWorker = self.getLast()


    def getFirstExecutingWorker(self):
        return self.firstExecutingWorker

    def getLastExecutingWorker(self):
        return self.lastExecutingWorker

    def getFirst(self):
        query = "select dagNode, executionHost, slotName, UNIX_TIMESTAMP(submitTime), UNIX_TIMESTAMP(executionStartTime), UNIX_TIMESTAMP(executionStopTime), UNIX_TIMESTAMP(terminationTime)  from submissions where dagNode != 'A' and executionStartTime !='0000-00-00 00:00:00' order by executionStartTime limit 1;"

        results = self.dbm.execCommandN(query)
        dbEntry = DbEntry(results[0])

        return dbEntry


    def getLast(self):
        query = "select dagNode, executionHost, slotName, UNIX_TIMESTAMP(submitTime), UNIX_TIMESTAMP(executionStartTime), UNIX_TIMESTAMP(executionStopTime), UNIX_TIMESTAMP(terminationTime) from submissions where dagNode != 'B' and executionStartTime !='0000-00-00 00:00:00' order by executionStopTime DESC limit 1;"

        results = self.dbm.execCommandN(query)
        dbEntry = DbEntry(results[0])

        return dbEntry

        