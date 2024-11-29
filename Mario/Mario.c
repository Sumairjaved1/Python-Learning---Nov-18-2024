// #include <cs50.h>
// #include <stdio.h>


// int main(void)
// {
//     int height, row, column, spacing;

//     do
//         {
//             height = get_int ("Enter Height: ");
//         }
//     while(height < 1 || height > 8);
    
//     for (row = 0; row < height; row++);
//         {
//         for (spacing = 0; spacing < height - row -1 ; spacing++)
//             printf(" ");
//         for (column = 0; column <= row; column++);
//             {
//                 printf("#");
//             }
//         printf("\n");    
//         }
// }


/////////////////////////////////////////////////////////
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height, row, column, spacing;

    // Prompt the user to enter a height between 1 and 8
    do
    {
        height = get_int("Enter Height: ");
    }
    while (height < 1 || height > 8);
    
    // Loop over each row
    for (row = 0; row < height; row++)
    {
        // Print the spaces
        for (spacing = 0; spacing < height - row - 1; spacing++)
        {
            printf(" ");
        }

        // Print the hashes
        for (column = 0; column <= row; column++)
        {
            printf("#");
        }

        // Move to the next line after each row
        printf("\n");
    }

    return 0;
}
