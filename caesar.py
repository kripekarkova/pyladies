#key a test if int
key = input('vložte klíč - pozitivní celé číslo: ')

try:
    key = int(key)
    if key < 0:
        print('Toto není kladné číslo')
        key_correct = False
        exit
    
    else:
        key_correct = True
        #print(key)
    
except:
    print('Toto není (celé) číslo')
    key_correct = False
    exit 



#šifra
ciphertext = ''
if key_correct:
    #plaintext - origo message 
    plaintext = input('vložte text, který má program zašifrovat: ')
    
    for p in plaintext:
        
        ciphertext += chr(ord(p) + key) 

    print('key: ', key, '\nplaintext: ', plaintext, '\nciphertext: ', ciphertext  )
    #překlad zpět
    prekladzpet = ''
    for r in ciphertext:
        
        prekladzpet += chr(ord(r) - key) 

    print('překlad zpět je ', prekladzpet)

else:
    print('klíč není dle očekávání, proto nic nebude')




    

