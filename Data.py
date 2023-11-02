from bs4 import BeautifulSoup as bs

class Data():
    def __init__(self, source: str, box):
        self.box = box[0]
        self.soup = bs(source, 'html.parser')
    def get_nonce(self) -> str:
        nonce = self.box.find_all('span', {'class': ''}).text

        return nonce


    def prettify(self):
        return self.box.apply(lambda x : bs(x, 'html.parser').prettify())
        
    def save_data(self):
        pass

    def __len__(self):
        return len(self.box)