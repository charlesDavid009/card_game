import numpy as np

class XORShift:
    def __init__(self, seed=1, word_length=64):
        self.sign_mask = (1 << (word_length-1))
        self.word_mask = self.sign_mask | (self.sign_mask -1)
        self.next = self._to2scomplement(seed)

    def _to2scomplement(self, number):
        return number & self.word_mask

    def _from2scomplement(self, number):
        return ~(number^self.word_mask) if (number & self.sign_mask) else number

    def seed(self, seed):
        self.next = self._to2scomplement(seed)

    def random(self):
        self.next ^= (self.next << 21) & self.word_mask
        self.next ^= (self.next >> 35) & self.word_mask
        self.next ^= (self.next <<  4) & self.word_mask
        return self._from2scomplement(self.next)

