object prob34 {
  def factorial(i: Int): Int = i match{
    case 0 => 1
    case 1 => 1
    case _ => i * factorial(i-1)
  }

  def digitFactorial(i: Int): Int = i match{
    case 0 => 0
    case _ => factorial(i%10) + digitFactorial(i/10)
  }

  def solve(i: Int): Int = i match {
    case 10000000 => 0
    //case digitFactorial(i) => 1 + solve(i+1)
    case _ if (digitFactorial(i) == i) => i + solve(i+1)
    case _ => solve(i+1)
  }

  def main(args: Array[String]){
    println(s"Sum: ${solve(10)}")
  }
}
