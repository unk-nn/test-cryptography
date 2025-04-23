# автор unk-nn & TonyLink TEAM

class Coderater():
    def __init__(self):
        # Словари кодирования для разных типов данных
        self.__coder_dID = {'o4D': 1, 'ti9': 2, 'TH2': 3, 'Fw7': 4, 'FDf': 5, 'Sl8': 6, 'JfV': 7, 'EE3': 8, 'NNg': 9, 'Tpp': 0}
        self.__coder_Uid1 = {'AtF': 1, '5LM': 2, 'llk': 3, 'jd0': 4, 'HHY': 5, 'iT1': 6, 'CTV': 7, 'XZ4': 8, 'ltd': 9, 'yJ2': 0}
        self.__coder_Uid2 = {'RvC': 1, 'GyL': 2, 'bPQ': 3, 'fWk': 4, 'pA8': 5, 'xN9': 6, 'zOI': 7, 'sE2': 8, 'JH3': 9, 'vq7': 0}
        self.__coder_dVOL = {'KxS': 1, 'QeU': 2, 'oZP': 3, 'dJa': 4, 'tH4': 5, 'mM5': 6, 'cB6': 7, 'pR8': 8, 'aV9': 9, 'yI0': 0, 'NI7':'.'}
        self.__codelDATS = {'LmF': 1, 'uRZ': 2, 'qDQ': 3, 'cXw': 4, 'vN5': 5, 'nM7': 6, 'gP8': 7, 'tC9': 8,
                                                'bO0': 9, 'zK1': 0, 'Xx6':'.', 'cEQ':'-', 'Oq3':':'}

        self.__codelTL1 = {'Uui': 'q', 'Hg0': 'w', 'NCV': 'e', 'Df7': 'r', 'Xzk': 't', 'LQ2': 'y', 'Yb4': 'u', 'Kt9': 'i',
                           'VmA': 'o', 'Rp3': 'p', 'Pz5': 'a', 'Bc6': 's', 'Mj1': 'd', 'Qn8': 'f', 'Tl3': 'g', 'Ws0': 'h', 'Zx9': 'j', 'Ry5': 'k', 'Fe7': 'l', 'Iq4': 'z',
                            'On6': 'x', 'Gh8': 'c', 'Sd2': 'v', 'Jb1': 'b', 'At3': 'n', 'Ew0': 'm', 'BBc': '-', 'Gsd':'_'}
        self.__codelTL2 = {'Ru1': 'q', 'Cm5': 'w', 'Nt9': 'e', 'Df3': 'r', 'Mk6': 't', 'Gh7': 'y', 'Vb8': 'u', 'Pn2': 'i',
                           'Jw4': 'o', 'Zp0': 'p', 'Aq3': 'a', 'Sx8': 's', 'Fe5': 'd', 'Hv1': 'f', 'Og2': 'g', 'Lj6': 'h',
                           'Ty9': 'j', 'Ui4': 'k', 'Kz7': 'l', 'Wd3': 'z', 'Bc0': 'x', 'Yr5': 'c', 'Xl8': 'v', 'Qn2': 'b', 'Ea6': 'n', 'Ih9': 'm', 'Bc6': '-', 'Tr2':'_'}
        self.__codel_fBOT = {'Az6': 'q', 'Wt7': 'w', 'Gs9': 'e', 'Bx0': 'r', 'Kn1': 't', 'Vh2': 'y', 'Ql3': 'u', 'Fd4': 'i',
                           'Ju5': 'o', 'Pc8': 'p', 'Yn9': 'a', 'Rm3': 's', 'Hb2': 'd', 'Lq7': 'f', 'Ie0': 'g', 'Tp4': 'h',
                           'Uk6': 'j', 'No5': 'k', 'Mr4': 'l', 'Zw9': 'z', 'Dg1': 'x', 'Xc7': 'c', 'Sv8': 'v', 'Al3': 'b', 'Oe0': 'n', 'Er8': 'm',
                            'YYt': '-', 'RF7':'_', 'ii5':'.', 'gBB':':', 'UuU':';', 'JiK': 1, 'vTs': 2, 'lPx': 3, 'eYg': 4, 'cHb': 5, 'aLo': 6,
                             'uMq': 7, 'rDw': 8, 'zFn': 9, 'pVr': 0}
        self.__codel_iBOT = {'Th9': 'q', 'Bw5': 'w', 'Hj4': 'e', 'Fl0': 'r', 'Sc3': 't', 'Km7': 'y', 'Vx1': 'u', 'Dp8': 'i', 'Qn2': 'o', 'Yg6': 'p', 'Lz9': 'a', 'Wu0': 's',
                           'Ar7': 'd', 'Ro4': 'f', 'Jv6': 'g', 'Em2': 'h', 'Cf5': 'j', 'Pd9': 'k', 'Nq1': 'l', 'Uy3': 'z',
                           'Gi2': 'x', 'Xp0': 'c', 'Zl5': 'v', 'In8': 'b', 'Mk3': 'n', 'Ob7': 'm', 'TFD': '-', 'OU7':'_', 'uy5':'.', 'BBg':':', 'IoI':';',
                            'eQj': 1, 'oGt': 2, 'zUw': 3, 'lDx': 4, 'bEa': 5, 'kFc': 6, 'mVd': 7, 'rNf': 8, 'pBv': 9, 'yGh': 0}

    # Внутренний метод кодирования значения через словарь
    def __coderr(self, f1, dictt):
        for i in str(f1):
            for key, val in dictt.items():
                if str(val) == i:
                    self.__fincod = self.__fincod + key
        self.__fincod = self.__fincod + '|'

    # Внутренний метод декодирования по 3 символа
    def __uncode(self, dl:int, dictr:dict):
        sek = 0
        vp = ''

        for i in self.__sdate[dl]:
            vp = vp + i
            sek = sek + 1

            if sek == 3:
                self.__finde = self.__finde + str(dictr[vp])
                sek = 0
                vp = ''
        self.__finde = self.__finde + '|'

    # Основной метод кодирования
    def encoder(self, dateID:int, dateUONE_id:int, dateUONE_cardTL:str, dateUTWO_id:int, dateUTWO_cardTL:str, DATEvol:float,
                 date:str, dateFROM_bot:str, dateIN_bot:str):
        self.__dID = dateID
        self.__duID1 = dateUONE_id
        self.__ucard1 = dateUONE_cardTL.lower()
        self.__duID2 = dateUTWO_id
        self.__ucard2 = dateUTWO_cardTL.lower()
        self.__dVOL = DATEvol
        self.__dats = date  # - исключение
        self.__dfBOT = dateFROM_bot.lower()
        self.__diBOT = dateIN_bot.lower()

        self.__fincod = '|'

        self.__coderr(self.__dID, self.__coder_dID)
        self.__coderr(self.__duID1, self.__coder_Uid1)
        self.__coderr(self.__ucard1, self.__codelTL1)
        self.__coderr(self.__duID2, self.__coder_Uid2)
        self.__coderr(self.__ucard2, self.__codelTL2)
        self.__coderr(self.__dVOL, self.__coder_dVOL)
        self.__coderr(self.__dats, self.__codelDATS)
        self.__coderr(self.__dfBOT, self.__codel_fBOT)
        self.__coderr(self.__diBOT, self.__codel_iBOT)

        return self.__fincod

    # Основной метод декодирования
    def decoder(self, Ckey:str):
        self.__finde = '|'
        self.__sdate = Ckey.split('|')

        try:
            self.__uncode(1, self.__coder_dID)
            self.__uncode(2, self.__coder_Uid1)
            self.__uncode(3, self.__codelTL1)
            self.__uncode(4, self.__coder_Uid2)
            self.__uncode(5, self.__codelTL2)
            self.__uncode(6, self.__coder_dVOL)
            self.__uncode(7, self.__codelDATS)
            self.__uncode(8, self.__codel_fBOT)
            self.__uncode(9, self.__codel_iBOT)

            return self.__finde
        except IndexError:
            return f'ErorrData // There is not enough data to decrypt :: {self.__finde}'

cc = Coderater()
print(cc.encoder(12, 923346567, 'User-TL',
               123234455, 'Unk-TL', 42.211, '12.03.2024-14:09:42', 'BitBot_2.0', 'Tezer2.0'))
print(cc.decoder(cc.encoder(12, 923346567, 'User-TL',
               123234455, 'Unk-TL', 42.211, '12.03.2024-14:09:42', 'BitBot_2.0', 'Tezer2.0')))
print('\n')