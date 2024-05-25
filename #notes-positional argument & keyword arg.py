#notes-positional argument & keyword argument
#positional argument 處理多餘的positional argument.
#寫任意數字的函式
def add(*args, **kwrgs):
    total = sum(args)
    return total
#    print(args)

result1 = add(1,2,3,4)
result2 = add(1,2,3,4,5)
result3 = add(1,2,3,4,5,6)
result4 = add(1,2,3,4,5,6,7)

print(result1)
print(result2)
print(result3)
print(result4)

#keyword argument 有值 的要放在後面, 處理多餘的keyword
def play_a_game( game_type, num_round=3, target_score=100):
    print(num_round, game_type, target_score)

play_a_game('pocker', target_score=300)

#開發套件會用到
def play_a_extra_game( game_type, num_round=3, target_score=100, **kwargs):
    print(num_round, game_type, target_score)

play_a_extra_game('pocker', gender=0, target_score=300) #有多餘的參數

def play_a_extra_game( game_type, num_round=3, target_score=100, **kwargs):
    if 'gender' is kwargs:
        print('game with gender')
    print(num_round, game_type, target_score, kwargs)

play_a_extra_game('pocker', gender=0)