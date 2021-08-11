from actors import Enemy, Player
import random
def main():
    print_intro()
    play()

def print_intro():
    print(
        '''
         Monster Slash !!!
         Ready Player One? Press [ENTER] to Continue ...
         '''
    )
    input()

def play():
    enemies = list()
    names = ['Akron', 'Jimpatchi', 'Gamichi', 'Lizan', 'Morales', 'Foster']
    for i in range(10):
        enemies.append(Enemy(kind=random.choice(names), level= random.randint(13,100)))
        
    players = list()
    pnames = ['Mohamed', 'Fank', 'Mike', 'Adam', 'Xin', 'Joanna']
    for j in range(10):
        players.append(Player(name=random.choice(pnames), level=random.randint(15,110)))
    
    print(players)
    print(enemies)

    while True:
        next_enemy = random.choice(enemies)
        next_player = random.choice(players)
        cmd = input('You are facing {}, Do you want to [r]un ? [a]ttack? [p]eace?'.format(next_enemy.kind))
        if cmd == 'a':
            print('attack the mothafucka {}'.format(next_enemy.kind))
            if next_player.attacks(next_enemy):
                enemies.remove(next_enemy)
                break
            else:
                print('{} Betta hide away, you lost to {} but you migh win at some point down the road'.format(next_player.name, next_enemy.kind))
        elif cmd == 'r':
            print('{} runs from the mothafucka {} his energy is {} and yours is {} with a {} diffrence against you'.format(next_player.name, next_enemy.kind, next_enemy.level, next_player.level, (next_enemy.level - next_player.level) ))
        elif cmd == 'p':
            print('{} you are a peaceful guy towards {} generally speaking'.format(next_player.name, next_enemy.kind))
        else:
            print('Yo!!! You Need to make a correct Option')
        print('*'*30)
        print()
        if not enemies:
            print('You win!!! Congratulations!')
            break

if __name__ == '__main__':
    main()