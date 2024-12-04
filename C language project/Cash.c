#include <stdio.h>
#include <cs50.h>
#include <math.h>

float askPositiveFloat(void)
{
    float PositiveFloat;
    bool negative = true;
    while (negative)
    {
        PositiveFloat = get_float("Change owed: ")
        
        if (PositiveFloat > 0)
        {
            negative = false
        }
    }
    return PositiveFloat;
}
int coinNum()
{
    int totalCents = round(askPositiveFloat() * 100);
    int numofCoins = 0;
    int remainder;
    int tempNum;
    int quarter = 25;
    int dime = 10;
    int nickel = 5;
    int penny = 1;

    if (totalCents >= quarter)
    {
        remainder = totalCents % quarter;
        tempNum = totalCents - remainder;
        numofCoins = numofCoins + (tempNum/quarter);
        totalCents = remainder;
    }
    if (totalCents >= dime)
    {
        remainder = totalCents % dime;
        tempNum = totalCents - remainder;
        numofCoins = numofCoins + (tempNum/dime);
        totalCents = remainder;
    }
    if (totalCents >= nickel)
    {
        remainder = totalCents % nickel;
        tempNum = totalCents - remainder;
        numofCoins = numofCoins + (tempNum/nickel);
        totalCents = remainder;
    }
    if (totalCents >= penny)
    {
        remainder = totalCents % penny;
        tempNum = totalCents - remainder;
        numofCoins = numofCoins + (tempNum/penny);
        totalCents = remainder;
    }
}

int main(void)
{
    printf("%i\n", coinNum());
}