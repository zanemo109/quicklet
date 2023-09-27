import openai
openai.api_key = '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'

test_words = "lend lease, maysville road veto, charles beard's constitution thesis, homestead strike, transcontinental railroads, california gold rush, jim crow laws, president lyndon b johnson, puritanism, election of 1800, greensboro sit-ins, dr. francis townsend, national road, federal employee loyalty program, clayton antitrust act, land ordinance and northwest ordinance, samuel gompers, declaration of independence, christopher columbus, bartolomeo de las casas, spanish empire, french empire, jamestown"
test_list = test_words.split(', ')
small = test_list[:3]

def list_to_string(list):
    words_string = ''
    for i in list:
        words_string += i + ', '
    return words_string[:-2]

def definitions_only(list):
    words_string = list_to_string(list)
    prompt = f'''
    
    Create me a list of definitions for the following words: {words_string}. Include ONLY the definitions, separated by semicolons.
    
    '''
    response = openai.Completion.create(engine = 'text-davinci-003', prompt = prompt, max_tokens=500)
    definition = response.choices[0].text.replace("\n\n", "").replace('•', '').replace("\n", ".")
    term_colon_def = definition.split(';')
    defs = []
    for card in term_colon_def:
        defs.append(remove_up_to_colon(card))
    return term_colon_def

def break_by_num(lst, num):
    lst = lst[:]
    if len(lst) <= num:
        return lst
    res = []
    while lst:
        new_lst = []
        while len(new_lst) < num:
            if lst:
                new_lst.append(lst.pop(0))
            else:
                res.append(new_lst)
                return res
        res.append(new_lst)
    return res

def apply_to_split(lst, func, num):
    if len(lst) <= num:
        return [func(i) for i in lst]
    else:
        lst = break_by_num(lst, num)
        res = []
        for i in lst:
            res.extend([func(j) for j in i])
        return res

def remove_up_to_colon(s):
    while ":" in s:
        s = s[1:]
    s = s[1:]
    return s
