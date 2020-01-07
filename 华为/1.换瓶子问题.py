# 编程题
# 有这样一道智力题：“某商店规定：三个空汽水瓶可以换一瓶汽水。小张手上有十个空汽水瓶，她最多可以换多少瓶汽水喝？”
# 答案是5瓶，方法如下：先用9个空瓶子换3瓶汽水，喝掉3瓶满的，喝完以后4个空瓶子，用3个再换一瓶，喝掉这瓶满的，这时候剩2个空瓶子。
# 然后你让老板先借给你一瓶汽水，喝掉这瓶满的，喝完以后用3个空瓶子换一瓶满的还给老板。
# 如果小张手上有n个空汽水瓶，最多可以换多少瓶汽水喝？

def change_bottle(n):
    total_drinked_bottle = 0
    left_bottle = n
    while left_bottle >= 3:
        drinked_bottle = left_bottle // 3 #先把3的整数倍喝了
        total_drinked_bottle += drinked_bottle # 又可以喝这么多
        left_bottle = left_bottle % 3 + drinked_bottle #剩余的瓶子数等于没换的+已经又喝的
        if(left_bottle==2): # 如果剩了2个瓶子 可以借一个
            left_bottle += 1
    return total_drinked_bottle

# assert change_bottle(0) == 0
# # assert change_bottle(3) == 1
# # assert change_bottle(10) == 5
# # assert change_bottle(81) == 40