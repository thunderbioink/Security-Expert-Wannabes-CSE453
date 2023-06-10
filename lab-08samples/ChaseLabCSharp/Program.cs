using System;
using System.Text.RegularExpressions;
using FluentValidation;


namespace ChaseLabCSharp;

class Program
{
    static void Main(string[] args)
    {
        SolutionOne();

        SolutionTwo();
    }

    private static void SolutionTwo()
    {
        // Ask for user input on what sports they like
        Console.WriteLine("What Sport do you like?");

        // Display the enum list to the user
        int index = 1;
        foreach (var sport in Enum.GetValues(typeof(SportsEnum)))
        {
            Console.WriteLine($"{index}. {sport}");
            index++;
        }
        
        var input = Console.ReadLine();
        // Use TryParse to make sure the integer is a valid integer
        if (int.TryParse(input, out int sportsNum))
        {
            // Check to see if the integer is found in the enum
            if (Enum.IsDefined(typeof(SportsEnum), sportsNum))
            {
                SportsEnum sport = (SportsEnum)sportsNum;
                System.Console.WriteLine($"The valid sport you chose is: {sport}");
            }
            else
            {
                Console.WriteLine("Not a valid input!");
            }
        }
        // This checks to see if the string is valid 
        else if (Enum.TryParse(input, out SportsEnum sport1))
        {
            // Checks the string to see if it is in the enum
            if (Enum.IsDefined(typeof(SportsEnum), sport1))
            {
                SportsEnum sport = sport1;
                System.Console.WriteLine($"The valid sport you chose is: {sport}");
            }
            else
            {
                Console.WriteLine("Not a valid input!");
            }
        }
        else
        {
            Console.WriteLine("Not a valid input!");
        }
    }

    static void Validate(Credentials creds)
    {
        Console.WriteLine($"Before Validation: \nUsername {creds.Username} \nPassword {creds.Password}\n");
        /* OUTPUT
            Before Validation: 
            Username chasemoses
            Password Padamah1025'; INSERT INTO passwordList (username, password) VALUES 'Chase', 'pass,
        */

        creds.Username = Regex.Replace(creds.Username, @"[^a-zA-Z0-9_]+", "");
        creds.Password = Regex.Replace(creds.Password, @"[^a-zA-Z0-9_]+", "");

        Console.WriteLine($"After Validation: \nUsername {creds.Username} \nPassword {creds.Password}");
        /* OUTPUT
            After Validation: 
            Username chasemoses
            Password Padamah1025INSERTINTOpasswordListusernamepasswordVALUESChasepass
        */
    }

    static void SolutionOne()
    {
        // Create a new credential object, passing in hardcoded username and password.
        Credentials credentials = new Credentials()
        {
            Username = "chasemoses",
            // Additional Statement attack
            Password = "Pickles2034'; INSERT INTO passwordList (username, password) VALUES 'Chase', 'pass"
        };

        CredentialValidator validator = new CredentialValidator();

        var results = validator.Validate(credentials);

        if(! results.IsValid) 
        {
            foreach(var failure in results.Errors)
            {
                Console.WriteLine("Property " + failure.PropertyName + " failed validation. Error was: " + failure.ErrorMessage);
            }
        }
    }
 
}
