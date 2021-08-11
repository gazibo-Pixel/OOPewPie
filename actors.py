from random import randint

class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return (
            'Player {} is at level {}'.format(self.name, self.level)
        )
    
    def get_attack_power(self):
        return randint(1,100)*self.level
    
    def attacks(self, enemy):
        power = self.get_attack_power()
        epower = enemy.get_attack_power()
        if power >= epower:
            print('You salivin {}'.format(enemy.kind))
            return True
        else:
            print('{} slayed {} '.format(enemy.kind, self.name))
        


class Enemy:
    def __init__(self, kind, level):
        self.kind = kind
        self.level = level
    
    def __repr__(self):
        return (
            'Enemy: {}, Enemy-Level: {}'.format(self.kind, self.level)
        )
    def get_attack_power(self):
        return randint(1,100)*self.level

if __name__ == '__main__':
    P300 = Player(name='Tashi', level=13)
    E300 = Enemy(kind='Ogre', level = 12)
    PX = P300.get_attack_power()
    EX = E300.get_attack_power()
    if PX > EX :
        print("{} win because it has {} excess".format(P300.name, (PX - EX)))
    else:
        print('{} win becuse it has {} excess power'.format(E300.kind, (EX - PX)))


    # print(P300)
    # print(E300)
    # print("The End!")