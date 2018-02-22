# Daniel Guerra Ramos Lopes  Nr Mecanografico 90590

# Variaveis --------
consoante = ("B", "C", "D", "F", "G", "H", "J", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "X", "Z")
par_consoantes = ("BR", "CR", "FR", "GR", "PR", "TR", "VR", "BL", "CL", "FL", "GL", "PL")
consoante_terminal = ("L", "M", "R", "S", "X", "Z")
consoante_final = ("N", "P") + consoante_terminal
vogal_palavra = ("A", "O", "E")
ditongo_palava = ("AI", "AO", "EU", "OU")
ditongo = ("AE", "AU", "EI", "OE", "OI", "IU") + ditongo_palava
par_vogais = ditongo + ("IA", "IO")
consoante_freq = ("D", "L", "M", "N", "P", "R", "S", "T", "V")
vogal = ("I","U")+ vogal_palavra

#Funcoes -----------
def e_silaba4(chars):
    """
    Funcao permite verificar se um dado conjunto de caracteres forma silaba valida de 4 letras
    """
    if type(chars) != str: # verifica se e uma string
        raise ValueError("e_silaba4:argumento invalido")
    if len(chars) == 4:
        # Confirma se tem 4 caracteres e verifica a sua validade de acordo com a gramática
        if chars[:2] in par_vogais and chars[2:] == "NS":
            return True
        elif chars[0] in consoante and chars[1] in vogal and (chars[2:] == "NS" or chars[2:] == "IS"):
            return True
        elif chars[:2] in par_consoantes and chars[2:] in par_vogais:
            return True
        elif chars[0] in consoante and chars[1:3] in par_vogais and chars[3] in consoante_final:
            return True #
        else:
            return False
    else: # Caso nao tenha 4 caracteres, entao a string nao e uma silaba4
        return False

def e_silaba5(chars):
    """
    Funcao permite verificar se um dado conjunto de caracteres forma silaba valida de 5 letras
    """
    if type(chars) != str: # Verifica se e string
        raise ValueError("e_silaba5:argumento invalido")
    if len(chars) == 5:
        if chars[:2] in par_consoantes and chars[2] in vogal and chars[3:] == "NS":
            return True # E valida se for par consoantes, vogal e "NS"
        else:
            return False
    else:
        return False

def e_monossilabo2(chars):
    """
    Funcao permite verificar se um dado conjunto de caracteres forma monossilabo valido de 2 letras
    """
    if type(chars) != str:  # Verifica se e string
        raise ValueError("e_monossilabo2:argumento invalido")
    if len(chars) == 2:
        # Confirma se tem 2 caracteres e verifica a sua validade de acordo com a gramática
        if chars[0:] in ("AR", "IR", "EM", "UM"):
            return True
        elif chars[0] in vogal_palavra and chars[1] == "S":
            return True
        elif chars[0:] in ditongo_palava:
            return True
        elif chars[0] in consoante_freq and chars[1] in vogal:
            return True
        else:
            return False
    else:
        return False

def e_monossilabo3(chars):
    """
    Funcao permite verificar se um dado conjunto de caracteres forma monossilabo valido de 3 letras
    """
    if type(chars) != str:# Verifica se e string
        raise ValueError("e_monossilabo3:argumento invalido")
    if len(chars) == 3: #Confirma se tem 3 caracteres e verifica a sua validade
        if chars[0] in consoante and chars[1] in vogal and chars[2] in consoante_terminal:
            return True
        elif chars[0] in consoante and chars[1:] in ditongo:
            return True
        elif chars[:2] in par_vogais and chars[2] in consoante_terminal:
            return True
        else:
            return False
    else:
        return False

def e_silaba(chars):
    """
    Funcao permite verificar se um conjunto de caracteres e uma silaba valida ate 5 letras
    """
    # Funcoes internas (apenas usadas dentro da funcao e_silaba)
    def e_silaba2(chars):
        """
        Funcao permite verificar se um dado conjunto de caracteres forma silaba valida de 2 letras
        """
        if (chars[0:2]) in par_vogais:  ## Se os dois primeiros caracteres juntos formarem um par_vogal valido
            return True
        elif chars[0] in consoante and chars[1] in vogal:  ## Se os dois primeiros caracteres formarem uma consoante e vogal,respetivamente
            return True
        elif chars[0] in vogal and chars[1] in consoante_final:  ## Se os dois primeiros caracteres formarem uma vogal e consoante_terminal
            return True
        else:
            return False

    def e_silaba3(chars):
        """
        Funcao permite verificar se um dado conjunto de caracteres forma silaba valida de 3 letras
        """
        if (chars[0:3]) in ("QUA", "QUE", "QUI", "GUE", "GUI"):  ## Se os tres primeiros (e unicos) caracteres estiverem no tuplo
            return True
        elif chars[0] in vogal and chars[1:] == "NS":
            return True
        elif chars[0] in consoante and chars[1:] in par_vogais:
            return True
        elif chars[0] in consoante and chars[1] in vogal and chars[2] in consoante_final:
            return True
        elif chars[0:2] in par_vogais and chars[2] in consoante_final:
            return True
        elif chars[0:2] in par_consoantes and chars[2] in vogal:
            return True
        else:
            return False

    if type(chars) != str:# Verifica se e string
        raise ValueError("e_silaba:argumento invalido")
    tam = len(chars)
    #Dependendo do tamanho da string, averigua se e uma silaba valida
    if tam == 1:
        if chars[0] in vogal:
            return True
        else:
            return False
    elif tam == 2:
        return e_silaba2(chars)
    elif tam == 3:
        return e_silaba3(chars)
    elif tam == 4:
        return e_silaba4(chars)
    elif tam == 5:
        return e_silaba5(chars)
    else:
        return False

def e_monossilabo(chars):
    """
    Funcao verifica se um conjunto de caracteres e um monossilabo valido
    """
    if type(chars) != str:# Verifica se e string
        raise ValueError("e_monossilabo:argumento invalido")
    tam = len(chars)
    # Dependendo do tamanho da string, averigua se e um monossilabo valido
    if tam == 1:
        if chars[0] in vogal_palavra:
            return True
        else:
            return False
    elif tam == 2:
        return e_monossilabo2(chars)
    elif tam == 3:
        return e_monossilabo3(chars)
    else:
        return False

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

    #se for monossilabo devolve True, caso contrario, vai testar a <silaba>*<silaba_final>
    if e_monossilabo(chars) == True:
        return True
    else:
        silaba_final_encontrada = False #Variavel q controla se foi encontrada uma silaba_final
        i = 5

        # Este while testa se nos ultimos 5 caracteres existe uma silaba_final
        # Quando encontrar uma silabafinal valida, remove essa silaba da string, e sai do while
        while i > 0:
            if e_silaba_final(chars[-i:]):
                chars = chars[:-i]
                silaba_final_encontrada = True
                break
            i -= 1

        # Caso tenha encontrado uma silaba final, vai verificar se a string sobrante e uma combinacao de silabas
        # Caso tenha encontrado e nao tenha sobrado nada, ou seja, len(chars) == 0, devolve True
        # Se nao encontrou uma silaba final, entao a string nao e uma palavra valida

        if silaba_final_encontrada == True:
            silabas_encontradas = 0
            tam = len(chars)
            if tam != 0:
                i = 0
                while i < tam:
                    for f in (5, 4, 3, 2, 1): #Testa do fim pro inicio se encontra uma silaba valida
                         if f <= len(chars):
                            if e_silaba(chars[-f:]):
                                silabas_encontradas += 1
                                chars = chars[:-f]
                                break
                    # Se apos a primeira iteracao nao encontrar silaba, entao a palavra nao e valida
                    if silabas_encontradas == 0:
                        return False
                    # Se tiver encontrado silabas, e o tamanho da string for 0, entao e uma palavra valida
                    elif silabas_encontradas > 0 and len(chars) == 0:
                        return True
                    i += 1
        #Se apos o while, len(chars) for > 0, entao e porque a string sobrante nao e composta apenas por silabas validas
        # Logo, devolve False
                if len(chars) > 0:
                    return False
            else:
                return True
        else:
            return False