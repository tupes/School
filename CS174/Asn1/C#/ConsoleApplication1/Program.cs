using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CS174
{
    class Asn1
    {
        static void Main(string[] args)
        {
            Q5();
        }

        // prompt for miles and gallons
        // print the mpg
        static void Q3()
        {
            double miles, gallons;
            while (true)
            {
                try
                {
                    miles = Convert.ToDouble(Console.ReadLine());
                    gallons = Convert.ToDouble(Console.ReadLine());
                }
                catch (FormatException)
                {
                    Console.WriteLine("Please enter only numbers");
                    continue;
                }
                string mpg = (miles / gallons).ToString();
                Console.WriteLine("You got " + mpg + " mpg on that tank.");
                Console.ReadLine();
                break;
            }
        }

        // prompt for centimetres
        // print the number of yards, feet, and inches
        static void Q5()
        {
            const double cmInInches = 2.54, inchesInYard = 36, inchesInFeet = 12;
            double cms, yards, feet, inches;
            while (true)
            {
                try
                {
                    cms = Convert.ToDouble(Console.ReadLine());
                }
                catch (FormatException)
                {
                    Console.WriteLine("Enter a number");
                    continue;
                }
                inches = cms / cmInInches;
                yards = Math.Floor(inches / inchesInYard);
                inches -= yards * inchesInYard;
                feet = Math.Floor(inches / inchesInFeet);
                inches -= feet * inchesInFeet;
                Console.WriteLine(yards.ToString() + " yards");
                Console.WriteLine(feet.ToString() + " feet");
                Console.WriteLine(inches.ToString() + " inches");
                Console.ReadLine();
                break;
            }
        }
    }
}
