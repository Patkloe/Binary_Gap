function binarygap(nbre){
 var nbrebin = Number(nbre).toString(2);
 var size = nbrebin.length;
alert("binary number : " + " " + nbrebin + " " + "taille : " + " " + size);
var i = 0;
var deb = 0;
var gap = 0;
var max = 0;
 if(nbrebin[deb] == 1){
    alert("debut comptage du gap");
    while(i < size){
      if(nbrebin[deb]!= nbrebin[i]){
          gap = i - deb;
          if(max < gap)
              max = gap;
      } // fin if
      else
         deb = i;
     i++;
    }//end while
 } // end if
console.log("binary gap : " + " " + max);
}
binarygap(17);
