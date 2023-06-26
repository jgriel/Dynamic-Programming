import sys

def kp_rec(c, items):
    if c < 0:
        return -9999
    if c == 0:
        return 0

    result = []
    for i in range(len(items)):
        tmp = list(items)
        tmp.remove(tmp[i]) 
        result.append(items[i][2] + kp_rec(c-items[i][1], tmp))
    
    max = 0
    for num in result:
        if num > max:
            max = num
        
    return max


def kp_dy(c, items):
    ops = {}
    ops[0] = (0, [])
    ops[1] = (15, [3])
    
    for i in range(2, c+1):
        highest = 0
        op_items = []
        for j in range(len(items)):
            if (i - items[j][1] >= 0) and (items[j][0] not in ops[i - items[j][1]][1]):
                tmp_items = []
                tmp_items.append(items[j][0])
                tmp = items[j][2] + ops[i - items[j][1]][0]
                tmp_items += ops[i - items[j][1]][1]
                if tmp > highest:
                    highest = tmp
                    op_items = list(tmp_items)
        ops[i] = (highest, op_items)   
    return ops[c]
    

if __name__ == "__main__":
    fn_in = sys.argv[1]
    fn_out = sys.argv[2]
    
    in_file = open(fn_in, 'r')
    out_file = open(fn_out, 'w')
    
    c = int(in_file.readline())
    
    items = []
    for line in in_file:
        tmp = line.split(', ')
        items.append((int(tmp[0]), int(tmp[1]), int(tmp[2])))
        
    # print(kp_rec(c, items))
    # print(kp_dy(c, items))
    
    val_items = kp_dy(c, items)
    
    out_file.write(str(val_items[0]) + ' ' + str(val_items[1]))
    
    
    

    

