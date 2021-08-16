# coding:gbk
from pygoogletranslation import Translator

tr = Translator()
print(tr.translate('星期日',dest='en').text)