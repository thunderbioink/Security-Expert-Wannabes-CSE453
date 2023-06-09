using System;
using System.Text.RegularExpressions;
using FluentValidation;


namespace ChaseLabCSharp;

class Program
{
    static void Main(string[] args)
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
 
}
