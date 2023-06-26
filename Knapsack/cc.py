import sys

def cc_rec(v, coins):
    if v < 0:
        return 9999
    if v == 0:
        return 0

    lowest = 999
    for i in range(len(coins)):
        temp = 1 + cc_rec(v-coins[i], coins)    
        lowest = min(temp, lowest)

    return lowest

def cc_dy(v, coins):
    v_coins = []
    v_coins.append(0)
    v_coins.append(1)

    for i in range(2, v+1):
        lowest = 999
        for j in range(len(coins)):
            if i - coins[j] >= 0:
                tmp = 1 + v_coins[i-coins[j]]
                lowest = min(tmp, lowest)
        v_coins.append(lowest)

    return v_coins[v]

def cc_dy_sol(v, coins):
    v_coins = {}
    default = {}
    for coin in coins:
        default[coin] = 0
        
    v_coins[0] = dict(default)
    v_coins[1] = dict(default)
    v_coins[1][1] = 1

    for i in range(2, v+1):
        c_amount = dict(default)
        c_amount[coins[0]] = 99999
        lowest_coin_amount = 99999
        for j in range(len(coins)):
            if i - coins[j] >= 0:
                tmp_coins = dict(v_coins[i-coins[j]])
                tmp_coins[coins[j]] += 1
                total_coins = sum(tmp_coins.values())
                if total_coins < lowest_coin_amount:
                    lowest_coin_amount = total_coins
                    c_amount = dict(tmp_coins)
        v_coins[i] = c_amount         
    return v_coins[v]

if __name__ == "__main__":
    fn_in = sys.argv[1]
    fn_out = sys.argv[2]
    
    in_file = open(fn_in, 'r')
    out_file = open(fn_out, 'w')
    
    value = int(in_file.readline())
    tmp = in_file.readline()
    tmp = tmp.replace('[', '')
    tmp = tmp.replace(']', '')
    coins = tmp.split(', ')
    for i in range(len(coins)):
        coins[i] = int(coins[i])
    
    # print(cc_rec(value, coins))
    # print(cc_dy(value, coins))
    
    coinage = cc_dy_sol(value, coins)
    
    out_file.write(str(coinage))
    
    

