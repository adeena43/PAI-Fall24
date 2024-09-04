def query(sentence):
    try:
        if sentence[len(sentence)-1] == '?':
            with open('question.txt', 'w') as fileObj:
                fileObj.write(sentence)
                print('It is a question!')
        else:
            print('The entered sentence is not a question!')
    except IOError as e:
        print(str(e))
    except Exception as a:
        print(str(a))

sentence = str(input('Please enter your sentence: '))

query(sentence)