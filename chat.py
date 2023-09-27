
def read_file(filename):
    chat_list = []
    with open(filename,'r',encoding = 'utf-8-sig') as ip:
        for line in ip:
            chat_list.append(line.strip())
    return chat_list
def convert(chat_list):
    new = []
    name = None
    for i in chat_list:
        if i == 'Allen':
            name = 'Allen'
            continue
        elif i == 'Tom':
            name = 'Tom'
            continue
        if name:
            new.append(name + ':' + i)
    return new
def write_file(filename,chat_list):
    with open(filename,'w',encoding = 'utf-8') as f:
        for x in chat_list: 
            f.write(x + '\n')
def main():
    chat_list = read_file('input.txt')
    chat_list = convert(chat_list)
    write_file('output',chat_list)
main()
