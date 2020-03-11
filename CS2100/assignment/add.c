#include <stdio.h>

int add(int num1[], int num2[], int res[])
{
    int i, c; //c is the carry in between 1-bit full adders
    int overflow;
    for (i = 15, c = 0; i >= 0; --i)
    {
        int s0 = num1[i] && !num2[i] || !num1[i] && num2[i]; //xor
        res[i] = s0 && !c || !s0 && c;                       //sum
        c = num1[i] && num2[i] || c && s0;                   //cout
    }
    //result += carry
    if (c)
    {
        for (i = 15; i >= 0; --i)
        {
            res[i] = !res[i];
            if (res[i] == 1)
            {
                break;
            }
        }
    }
    overflow = !num1[0] && !num2[0] && res[0] || num1[0] && num2[0] && !res[0];
    return overflow;
}

int addCorrect(int num1[], int num2[], int res[])
{
    int i, carry = 0, value, sign1 = num1[0], sign2 = num2[0], signR;
    for (i = 15; i >= 0; i--)
    {
        value = num1[i] + num2[i] + carry;
        if (value > 1)
        {
            value = value - 2;
            carry = 1;
        }
        else
        {
            carry = 0;
        }
        res[i] = value;
    }
    for (i = 15; i >= 0; i--)
    {
        value = res[i] + carry;
        if (value > 1)
        {
            value = value - 2;
            carry = 1;
        }
        else
        {
            carry = 0;
        }
        res[i] = value;
    }
    signR = res[0];
    if (sign1 == sign2 && sign1 != signR)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

//increment the number by 1 (treated as unsigned)
//returns 1 if overflow
int plusOne(int *num)
{
    int i;
    for (i = 15; i >= 0; --i)
    {
        if (num[i] == 1)
            num[i] = 0;
        else
        {
            num[i] = 1;
            break;
        }
    }
    return (i == -1);
}

//returns 1 if two numbers are equal, 1 otherwise
//c1 and c2 are the overflow flag
int areEqual(int *num1, int *num2, int c1, int c2)
{
    for (int i = 0; i < 16; i++)
    {
        if (num1[i] != num2[i])
            return 0;
    }
    return (c1 == c2);
}

//print number
void printNum(int *num)
{
    for (int i = 0; i < 16; ++i)
    {
        printf("%d", num[i]);
    }
    printf("\n");
}

int zero[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int num1[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int num2[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int resa[16];
int resb[16];

int main()
{
    int wrong_count = 0;
    do
    {
        do
        {
            int r1 = add(num1, num2, resa);
            int r2 = addCorrect(num1, num2, resb);
            if (areEqual(resa, resb, r1, r2))
            {
                /*
                printf("Correct!\n");
                printNum(num1);
                printNum(num2);
                printNum(resa);
                printNum(resb);
                printf("\n");
                getchar();
                */
                continue;
            }
            else
            {
                printf("Wrong result, next 5 lines show the operands, wrong sum correct sum, wrong overflow and correct overflow...\n");
                printNum(num1);
                printNum(num2);
                printNum(resa);
                printNum(resb);
                printf("%d, %d\n", r1, r2);
                ++wrong_count;
                printf("\n");
                getchar();
            }
        } while (!plusOne(num2));
        printf("Done for ");
        printNum(num1);
    } while (!plusOne(num1));

    printf("Done!\n");
    printf("Totally %d wrong\n", wrong_count);

    return 0;
}