from fastai.text import *
import sentencepiece as spm

class BengaliTokenizer(BaseTokenizer):
    def __init__(self, lang:str):
        self.lang = lang
        self.sp = spm.SentencePieceProcessor()
        self.sp.Load("/home/gaurav/PycharmProjects/nlp-for-bengali/tokenizer/bengali_lm.model")
        
    def tokenizer(self, t:str) -> List[str]:
        return self.sp.EncodeAsPieces(t)
