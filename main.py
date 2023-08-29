import pandas as pd

df = pd.read_csv('hotels.csv', dtype={'id': str})
df_cards = pd.read_csv('cards.csv', dtype=str).to_dict(orient='records')

class Hotel:
    def __init__(self, id):
        self.id = id
        self.name = df.loc[df['id'] == self.id, 'name'].squeeze()

    def book(self):
        df.loc[df['id'] == self.id, 'available'] = 'no'
        df.to_csv('hotels.csv', index=False)

    def available(self):
        availability = df.loc[df['id'] == self.id, 'available'].squeeze()
        if availability == 'yes':
            return True
        else:
            return False


class ReservationTicket:

    def __init__(self, customer_name, hotel):
        self.customer_name = customer_name
        self.hotel = hotel

    def reservation(self):
        content = f"""
        Thank you for your reservation.
        Here is your booking ticket:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name} 
        """
        return content


class CreditCard:
    def __init__(self, card_number, expiration, holder, ccv):
        self.card_number = card_number
        self.expiration = expiration
        self.holder = holder
        self.ccv = ccv

    def validate(self):
        card = {'number': self.card_number, 'expiration': self.expiration,
                'holder': self.holder, 'ccv': self.ccv}
        if card in df_cards:
            return True
        else:
            return False

class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = 'example'
        return password == given_password


print(df)

hotel_id = input('Enter the id of the hotel: ')
hotel = Hotel(hotel_id)

if hotel.available():
    card_number = input('Enter your credit card number: ')
    expiration = input("Enter expiration date: ")
    holder = input("Enter card holder: ")
    ccv = input("Enter ccv code: ")
    credit_card = SecureCreditCard(card_number, expiration, holder, ccv)
    if credit_card.validate():
        password = input('Enter payment password: ')
        if credit_card.authenticate(given_password=password):
            hotel.book()
            name = input("Enter your name: ")
            ticket = ReservationTicket(name, hotel)
            print(ticket.reservation())
        else:
            print('Credit card authentication failed.')
    else:
        print('Sorry, your card is invalid.')
else:
    print("Hotel is all booked for now.")


