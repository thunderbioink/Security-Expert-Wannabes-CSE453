using FluentValidation;
using System.Text.RegularExpressions;

namespace ChaseLabCSharp;


public class Credentials
{
    public string Username { get; set; }
    public string Password { get; set; }

}

class CredentialValidator : AbstractValidator<Credentials>
{
    public CredentialValidator()
    {
        // Require Username
        RuleFor(x => x.Username).NotEmpty().WithMessage("Needs to have a value!");
        RuleFor(x => x.Username).Matches(@"[a-zA-Z0-9_]+$").WithMessage("Username cannot contain special characters!");

        // Require Password
        RuleFor(x => x.Password).NotEmpty();

        // Length must be between 6 and 15 in length
        RuleFor(x =>x.Password).Length(6,15).WithMessage("Password cannot be shorter than 6 characters or longer than 15!");
        RuleFor(x =>x.Password).Matches(@"[a-zA-Z0-9_]+$").WithMessage("Password cannot contain special characters!");
    }      
   
}