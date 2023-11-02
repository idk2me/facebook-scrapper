from bs4 import BeautifulSoup as bs

class Data():
    def __init__(self, box: str):
        self.box = bs(box, 'html.parser')

    def get_nonce(self) -> str:
        return self.box.script['nonce']

    def prettify(self):
        return self.box.apply(lambda x : self.box.prettify())
        
    def save_data(self):
        pass

    def __len__(self):
        return len(self.box)