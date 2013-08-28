class Player:
   
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.rounds = ['RM','PM','B','T','D','L','IC']
        self.score = int(0)
       
    def player_needs(self,full_hand):
        return full_hand - len(self.hand)
       
    def get_hand(self):
        return self.hand
       
    def play_hand(self, deck, round_name, card_list):
       
        self.rounds.remove(round_name)
        
        #card list can be structured list of lists
        cards_in_hand = [item for sublist in card_list for item in sublist]
        deck.all_melds += cards_in_hand
        self.score += self.hand_score(round_name,card_list, all_melds)
        
        for card in cards_in_hand:

            self.hand.remove(card)
            deck.append(card)
   
    def face_val(card):
        if card[:-1] in ["q","k","j"]:
           return int(10)
        elif card[:-1] == "a":
           return int(1)
        elif int(card[:-1]) in range(2,11):
           return int(card[:-1])
          
    def hand_score(self,round_name,card_list, all_melds):
        round_name = round_name.lower()
        score = 0
       
        if round_name == 'rm':
            for card in card_list:
                score -= self.face_val(card)
       
        if round_name == 'pm':
            for card in card_list:
                if card[1] != "s":
                    card_list.remove(card)
           
            for card in card_list:
                score += self.face_val(card)
       
        if round_name == 'b':
            other_cards = all_melds
           
            for card in card_list:
                other_cards.remove(card)
            
            for card in card_list:
                curr_suit = card[1]
                for other in other_cards:
                    if other[1] == curr_suit:
                        score += 2
            
        if round_name == 't':
            score += self.face_val(card)
            
        if round_name == 'd':
            suits = FreqDist([item[1] for item in card_list])
            if 'a' in [item[0] for item in card_list] and 'h' in suits.keys():
                score = suits.count(suits.max())*10
        
        if round_name == 'l':
            score = sum([self.face_val(item[0]) for item in card_list])
            if score != 25:
                score = 0
        
        if round_name == 'ic':
            # get score for ones digit
            score += int(str(sum([self.face_val(card) for card in card_list[1]]))[-1])
            
            # get score for poker hand 
            score += deck.poker_hand(card_list[0])
        
        return score
