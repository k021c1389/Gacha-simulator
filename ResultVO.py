class ResultVO(object):
    def __init__(self):
        self._total_count = 0
        self._price = 0
        self._1_gacha_count = 0
        self._11_gacha_count = 0
        self._gacha_rireki = {
          "N": [],
          "N+": [],
          "R": [],
          "R+": [],
          "SR": [],
          "SR+": []
        }

    def get_total_count(self):
        return self._total_count

    def set_total_count(self, count):
        self._total_count = count

    def get_1_gacha_count(self):
        return self._1_gacha_count

    def set_1_gacha_count(self, count):
        self._1_gacha_count = count

    def get_11_gacha_count(self):
        return self._11_gacha_count

    def set_11_gacha_count(self, count):
        self._11_gacha_count = count

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def get_gacha_rireki(self):
        return self._gacha_rireki

    def set_gacha_rireki(self, gacha_rireki):
        self._gacha_rireki = gacha_rireki


    total_count = property(get_total_count, set_total_count)
    single_gacha_count = property(get_1_gacha_count, set_1_gacha_count)
    eleven_gacha_count = property(get_11_gacha_count, set_11_gacha_count)
    price = property(get_price, set_price)
    gacha_rireki = property(get_gacha_rireki, set_gacha_rireki)

