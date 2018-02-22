# Programming Fundamentals 1st Project _ in C

``` While(True): 
      Programming is Fun!
``` 
![](http://www.tu-berlin.de/fileadmin/a70100710_summeruniversity/summerschools/course-java.png)

## BETA

### Version 1.0

This version is the very first version. 
Very early stages.

## Motivation

This project is the conversion of the project1.py file to C.

#### Small code sample:
```
def e_palavra(chars):
    """
    Funcao que avalia se um dado conjunto de caracteres e uma palavra valida
    """
    #Funcao interna
    def e_silaba_final(chars):
        """
        Funcao que avalia se um dado conjunto de caracteres e uma silaba_final valida
        """
        #So fara sentido se for pelo menos 2 caracteres, caso tenha, ira testar a sua validade
        # Silaba_final e valida se for monossilabo2,3 ou silaba4,5

        if len(chars) >= 2:
            if e_monossilabo2(chars) or e_monossilabo3(chars):
                return True
            elif e_silaba4(chars) or e_silaba5(chars):
                return True
            else:
                return False
        else:
            return False

    if type(chars) != str:# Verifica se e string
        raise ValueError("e_palavra:argumento invalido")
```

## Any Suggestions?
Feel free to comment down below.


