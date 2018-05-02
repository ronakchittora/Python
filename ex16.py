from random import sample, choice, randint, shuffle

def gen_password(type):
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = '0123456789'
    c = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    d = '~!@#$%^&*-_'
    word = ''
    if type == 'weak':
        word_list = sample(a,8)
        for i in word_list:
            word += i
        return word
    elif type == 'medium':
        #1 letters, numbers
        len_total = randint(8,12)
        len_char = len_total - randint(1,6)
        len_digit = len_total - len_char
        word_list = sample(a,len_char)
        digits = sample(b,len_digit)
        pass_list = word_list + digits
        shuffle(pass_list)
        for i in pass_list:
            word += i
        return word
    elif type == 'strong':
        # lc up letters, numbers, special characters
        len_char = randint(4,12)
        len_char_up = len_char - randint(1,4)
        len_char_lw = len_char - len_char_up
        len_sp = randint(1,3)
        len_digit = randint(1,16-len_char-len_sp)
        word_list_lw = sample(a,len_char_lw)
        word_list_up = sample(c,len_char_up)
        digits = sample(b,len_digit)
        sp_ch = sample(d,len_sp)
        pass_list = word_list_lw + digits + word_list_up + sp_ch
        shuffle(pass_list)
        for i in pass_list:
            word += i
        return word
