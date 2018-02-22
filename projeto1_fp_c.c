#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

/*Words' grammar defined by lists/arrays*/

/* Variables -------- */
consoante = ["B", "C", "D", "F", "G", "H", "J", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "X", "Z"]
par_consoantes = ["BR", "CR", "FR", "GR", "PR", "TR", "VR", "BL", "CL", "FL", "GL", "PL"]
consoante_terminal = ["L", "M", "R", "S", "X", "Z"]
consoante_final = ["N", "P"] + consoante_terminal
vogal_palavra = ["A", "O", "E"]
ditongo_palava = ["AI", "AO", "EU", "OU"]
ditongo = ["AE", "AU", "EI", "OE", "OI", "IU"] + ditongo_palava
par_vogais = ditongo + ["IA", "IO"]
consoante_freq = ["D", "L", "M", "N", "P", "R", "S", "T", "V"]
vogal = ["I","U"]+ vogal_palavra

/* Functions */

char e_silaba4(char chars){
  /*TEST*/
}

/* Main */

int main(int argc, char const *argv[]) {
  /* code */
  return 0;
}
