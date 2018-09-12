/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 /
package fibonacci;

import java.util.;
import java.math.*;

/
 *
 * @author FUYU
 */
public class Fibonacci {

    /
     * @param args the command line arguments
     */
    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Ingrese el numero de fibonacci ");
        int fib = scanner.nextInt();
        int num = 0;
        int num2 = 1;
        int num3 = 0;

        for (int i = 0; i < fib-1; i++) 
        {
            num3 = num+num2;
            num = num2;
            num2 = num3;
        }
        System.out.println("Resultado: " + num3);
        System.out.println("byte = 13th para overflow");
        System.out.println("short = 24th para overflow");
        System.out.println("Int = 47th para overflow");     
        System.out.println("long = 93th para overflow");
        System.out.println("BigInt = Limite por Memoria para overflow");
    }
}
