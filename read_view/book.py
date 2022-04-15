import ebooklib
from ebooklib import epub
import os.path
from bs4 import BeautifulStoneSoup

BOOK_FORMAT = ['.epub','.txt','.pdf','.mobi','.azw3']
class Book():
    def __init__(self, path):
        f = os.path.splitext(path)[1]
        if f not in BOOK_FORMAT:
            raise TypeError('不支持此格式')
        self.path = path
        self.format = f

    def get_chapter(self):
        if self.format == '.epub':
            return self._get_epub_chapter()

    def _get_epub_chapter(self):
        book = epub.read_epub(self.path)
        ncx = book.get_item_with_id('ncx').content.decode()
        ncx_bs = BeautifulStoneSoup(ncx)
        chapter = {nav.navLabel.text : nav.content['src'] for nav in ncx_bs.findAll('navMap')[0].findAll('navPoint')}
        return chapter

if __name__ == '__main__':
    book = Book('resource\小王子.epub')
    for x in book.get_chapter():
        print('那就是电脑上看今年是可能是可能的看！！！！')
        print(x)
