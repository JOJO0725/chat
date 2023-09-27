
def read_file(filename):
    chat_list = []
    with open(filename,'r',encoding = 'utf-8-sig') as ip:
        for line in ip:
            chat_list.append(line.strip())
    return chat_list
def convert(chat_list):    
    name = None
    Allen_wordcount = 0
    Allen_photo = 0
    Viki_wordcount = 0
    Viki_photo = 0
    Allen_emoji = 0
    Viki_emoji = 0
    for i in chat_list:
        s = i.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                Allen_emoji += 1
            elif s[2] == '圖片':
                Allen_photo += 1
            else:
                for m in s[2:]:
                    Allen_wordcount = Allen_wordcount + len(m)
        elif name == 'Viki':
            if s[2] == '貼圖':
                Viki_emoji += 1
            elif s[2] == '圖片':
                Viki_photo += 1
            else:
                for m in s[2:]:
                    Viki_wordcount = Viki_wordcount + len(m)
    print('Allen說了:',Allen_wordcount,'字!','傳了', Allen_emoji,'張貼圖',Allen_photo,'張圖片')
    print('Viki說了:',Viki_wordcount, '字!','傳了', Viki_emoji,'張貼圖',Viki_photo,'張圖片')             
def write_file(filename,chat_list):
    with open(filename,'w',encoding = 'utf-8') as f:
        for x in chat_list: 
            f.write(x + '\n')
def main():
    chat_list = read_file('LINE-Viki.txt')
    chat_list = convert(chat_list)
    # write_file('output',chat_list)
main()
