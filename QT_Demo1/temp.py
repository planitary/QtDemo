# coding:gbk
from pygoogletranslation import Translator

tr = Translator()
print(tr.translate('������',dest='en').text)