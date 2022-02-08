class Record:
    def __init__(self, bs, is_, fs, rm):
        self.back_sight = bs
        self.inter_sight = is_
        self.fore_sight = fs
        self.remark = rm
        self.tbm = None
        self._convertToFloat()
        self._extractTBM()

    def _convertToFloat(self):
        self.back_sight = float(self.back_sight) if self.back_sight != '' else None
        self.fore_sight = float(self.fore_sight) if self.fore_sight != '' else None
        self.inter_sight = float(self.inter_sight) if self.inter_sight != '' else None

    def _extractTBM(self):
        if 'tbm' in self.remark.lower():
            self.tbm = self.remark.lower().strip('tbm')
            self.tbm = float(self.tbm)
        # return self.tbm
