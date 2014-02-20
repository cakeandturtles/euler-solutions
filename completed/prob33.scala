object prob33 {
  def main(args: Array[String]){
    for (d <- 10 to 99){          //Loop for the denominator
      for (n <- 10 to d){         //Loop for the numerator (always <= denominator)
        if (!(n%10==0 && d%10==0) && !(n%11==0 && d%11==0) && n/d!=1){
          val n1 = n/10; val n2 = n%10;
          val d1 = d/10; val d2 = d%10;
          val value = n.toFloat/d;
          var v1 = n1.toFloat/d1;
          if (v1 == value && n2==d2){
            println(s"$n/$d, ${n1}/${d1}");
          }else{
            var v2 = n1.toFloat/d2;
            if (v2 == value && n2==d1){
              println(s"$n/$d, ${n1}/${d2}");
            }
            else{
              var v3 = n2.toFloat/d1;
              if (v3 == value && n1==d2){
                println(s"$n/$d, ${n2}/${d1}");
              }
              else{
                var v4 = n2.toFloat/d2;
                if (v4 == value && n1==d1){
                  println(s"$n/$d, ${n2}/${d2}");
                }
              }
            }
          }
        }
      }
    }
  }
}
