class Deck:
    def __init__(self):
        self.vals = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
        self.suits = ["s","c","d","h"]
        self.deck =  [x+y for x in vals for y in suits]
      
         
    def shuffle(self):
        self.deck = random.shuffle(self.deck)
      
         
    def deal(self, players, total_cards):
        for player in players:
            cards_needed = player.player_needs()
            while cards_needed > 0:
                self.give_card(player,self.deck.pop(0))
                cards_needed -= 1
    
    
    def give_card(self,player,card):
        player.hand.append(card)
      
        
    def is_straight(card_list):
        '''
        checks whether the current hand is a straight.
        '''
        acehigh_list = []
        acelow_list = []
        for x in card_list:
		    #translate face cards to numeric values
            if x[0] == 'j':
                acehigh_list.append(11)
                acelow_list.append(11)
            elif x[0] == 'q':
                acehigh_list.append(12)
                acelow_list.append(12)
            elif x[0] == 'k':
                acehigh_list.append(13)
                acelow_list.append(13)
            elif x[0] == 'a':
                acehigh_list.append(14)
                acelow_list.append(1)
            elif int(x[:-1]) in [2,3,4,5,6,7,8,9,10]:
                acehigh_list.append(int(x[0]))
                acelow_list.append(int(x[0]))
           
        acehigh_list.sort()
        acelow_list.sort()

        #get diffs between number and its neighbor
        lowdiff_set = set([acelow_list[x]-acelow_list[x-1] for x in range(1,len(acelow_list))])
        highdiff_set = set([acehigh_list[x]-acehigh_list[x-1] for x in range(1,len(acehigh_list))])

	      #if all diffs are 1, the hand is a straight
        if len(lowdiff_set)==1 and 1 in lowdiff_set:
            return True
        elif len(highdiff_set)==1 and 1 in highdiff_set:
            return True
        else:
            return False

    def poker_score(card_list):
         
        numbers = [item[0] for item in card_list]
        freq_nums = FreqDist(numbers)
        suits = [item[1] for item in card_list]
        freq_suits = FreqDist(suits)
         
        isStraight = deck.is_straight(card_list)
         
        # flush
        if 5 in freq_suits.values():
            if is_Straight:
                return royal_flush_val
            else:
                return flush_val
        if 4 in freq_nums.values():
            return 4ofkind_val
        if 3 in freq_nums.values() and 2 in freq_nums.values():
            return fullhouse_val
        if is_Straight:
            return straight_val
        if 3 in freq_nums.values():
            return 3ofkind_val
        if freq_nums.values[0] == 2 and freq_nums.values[1] == 2:
            return 2pair_val
        if freq_nums.values[0] == 2:
            return pair_val
        else:     
            return 0
