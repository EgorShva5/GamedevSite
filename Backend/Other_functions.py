import string, random

def GenPassword(lenght):
    list_symb = string.ascii_letters+string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
    new_pass = ''.join(random.choice(list_symb) for i in range(lenght))
    
    return new_pass


d =   {'а' : ['а', 'a', '@'],
  'б' : ['б', '6', 'b'],
  'в' : ['в', 'b', 'v'],
  'г' : ['г', 'r', 'g'],
  'д' : ['д', 'd'],
  'е' : ['е', 'e','ie'],
  'ё' : ['ё', 'e'],
  'ж' : ['ж', 'zh', '*'],
  'з' : ['з', '3', 'z'],
  'и' : ['и', 'u', 'i'],
  'й' : ['й', 'u', 'i'],
  'к' : ['к', 'k', 'i{', '|{'],
  'л' : ['л', 'l', 'ji'],
  'м' : ['м', 'm'],
  'н' : ['н', 'h', 'n'],
  'о' : ['о', 'o', '0'],
  'п' : ['п', 'n', 'p'],
  'р' : ['р', 'r', 'p'],
  'с' : ['с', 'c', 's'],
  'т' : ['т', 'm', 't'],
  'у' : ['у', 'y', 'u'],
  'ф' : ['ф', 'f'],
  'х' : ['х', 'x', 'h' , '}{'],
  'ц' : ['ц', 'c', 'u,'],
  'ч' : ['ч', 'ch'],
  'ш' : ['ш', 'sh'],
  'щ' : ['щ', 'sch'],
  'ь' : ['ь', 'b'],
  'ы' : ['ы', 'bi'],
  'ъ' : ['ъ'],
  'э' : ['э', 'e'],
  'ю' : ['ю', 'io'],
  'я' : ['я', 'ya', 'ya']
}

BadWords = open('profanity_list/true_list.txt', 'r', encoding='UTF-8').read().split('\n')

def CheckText(Text):
    test_text = Text.lower()
    
    for key, value in d.items():
        for letter in value:
           #print(test_text)
            for num, let in enumerate(test_text):
                #print(num, let)
               # print(test_text)
                try:
                    ml = [test_text[num-1]+let+test_text[num+1],let+test_text[num+1],test_text[num-1]+let, let]
                    for i in ml:
                        if i == letter:
                            test_text = test_text.replace(i, key)
                            break
                except:
                    if let == letter:
                        test_text = test_text.replace(letter, key)
        
    #print(test_text)  
    new_t = test_text.split()
    
    for word in BadWords:
        for fragment in new_t:
            #print(fragment)
            if fragment in BadWords:
                return True
    
    return False