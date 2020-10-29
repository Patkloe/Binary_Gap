function dec2bin(dec){
    return Number(dec).toString(2);
} // function to convert a number to a binary value.

let t=dec2bin(8);  let s=t.length; console.log("size string" + " " + s + " "+ "binary number :" + " " + t +"\n");
// now get to code the gab between binary value generated 
let deb = 0; // pour initialiser le compteur
let max = 0; // qui se changera
let maxv=0;
if (t[deb]=="1")  // all number, binary starts with 1
   console.log("start point");
   let size = 1;
   while(size < s )  // making a loop to navigate on other binary values of the number generated.
        {
          if(t[deb] != t[size])  //start the first binary value of the array , then size = deb + 1, si difference trouvee
           {
            // ici faut mettre le while
             maxv = size-deb; // quand on a une difference, on fait une mise a jour du nombre de valeurs pour le gap
             if(maxv > max)  // on compare cette valeur a la valeur maximale deja storee, on fait une mise a jour
               {
                 max = maxv;
               }
            }
         else if(t[deb] == t[size]) //si egalite trouvee, on fait la mise a jour de la valeur ou on commence a faire descomparaisons
            {
             deb == size;  // pour controle
             maxv = 0;
            if(maxv > max)
               {
                 max = maxv;
               }
           }
         size++;  
        }
