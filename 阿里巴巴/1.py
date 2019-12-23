
# 给一个英文文本“i have a dream i am a human you can have dream too.”再给一个文本“i you am ”，
# 要求计算出第一个文本中包含第二个文本每个单词的最短文本，比如例子中最短文本就是“i am a human you”。

def search_short_text(text,find_text):
    text_word = text.split(" ")
    find_text_word = find_text.split(" ")
    text_seq_len = len(text_word) #截取的text长度
    text_seq = ""
    for i in range(len(text_word)):
        for j in range(i+1,len(text_word)+1):
            word_in = True
            text_seq_word = text_word[i:j] # 当前截取的text
            for word in find_text_word:
                if word not in text_seq_word:
                    word_in = False
                    break
            if not word_in:
                pass
            else:
                if j-i < text_seq_len:
                    text_seq_len = j - i
                    text_seq = " ".join(text_seq_word)
    return  text_seq

assert(search_short_text("i have a dream i am a human you can have dream too.","i you am")=="i am a human you")
assert(search_short_text("ILM runs a batch processing environment capable of modeling, rendering and compositing tens of thousands of motion picture frames per day. Thousands of machines running Linux, IRIX, Compaq Tru64, OS X, Solaris, and Windows join together to provide a production pipeline used by ~800 users daily. Speed of development is key, and Python was a faster way to code (and re-code) the programs that control this production pipeline.","a of")=="a batch processing environment capable of")

#
# 下面是面试者给出的答案:最优路径规划
#

def lengthCa(arr):
    start = arr[0]
    end = arr[0]
    for i in arr:
        if i > start:
            start = i
        if i < end:
            end = i
    return start - end


# 输入的第一个文本
text = 'ILM runs a batch processing environment capable of modeling, rendering and compositing tens of thousands of motion picture frames per day. Thousands of machines running Linux, IRIX, Compaq Tru64, OS X, Solaris, and Windows join together to provide a production pipeline used by ~800 users daily. Speed of development is key, and Python was a faster way to code (and re-code) the programs that control this production pipeline.'
# 输入的第二个文本
keywords = 'a of'
newtext = text.split(' ')
newkeys = keywords.split(' ')
textLen = len(newtext)
array = []
# 把index计算出来，用做最优路径规划使用
for i in newkeys:
    dan = []
    for j in range(textLen):
        if i == newtext[j]:
            dan.append(j)
    array.append(dan)
print(array)
# 最优规划开始
caculateArray = []
for n in array[0]:
    temp = []
    temp.append(n)
    caculateArray.append(n)
flag = 0
for n in array:
    if array.index(n) == 0:
        continue
    temparr = []

    for m in caculateArray:  # 遍历当前最短路径
        index = caculateArray.index(m)  # 计算当前路径的index值
        tempminlen = 1000000
        tempminarr = []
        for j in n:  # 计算当前最短路径，添加下一个节点
            if flag == 0:
                temparr.append(m)
            else:
                for x in m:
                    temparr.append(x)
            temparr.append(j)

            if lengthCa(temparr) < tempminlen:
                tempminlen = lengthCa(temparr)
                tempminarr = temparr
            temparr = []
        caculateArray[index] = tempminarr
        print(caculateArray)
    flag += 1
tempminlen = 1000000
tempminarr = []
# 找出最终所有解里的最优解，为tempminarr
for n in caculateArray:
    if lengthCa(n) < tempminlen:
        tempminlen = lengthCa(n)
        tempminarr = n
# 计算tempminarr的起点和重点，现在发现用min()和max()函数就可以了
start = tempminarr[0]
end = tempminarr[0]
for i in tempminarr:
    if start < i:
        start = i
    if end > i:
        end = i
# 输出起始位置和终止位置
print(start, end)
for m in range(end, start + 1):
    print(newtext[m])