#include<stdio.h>

int main()
{
    int a[100],b[100],c[100],i,j,s,p,count,n;
    printf("Enter data size: ");
    scanf("%d",&n);
    printf("Enter data in binary: ");
    for(i=0; i<n; i++)
    {
        scanf("%d",&a[i]);
    }

    i=0;
    j=0;

    count = 0;

    while(i<n)
    {
        if(a[i]==1)
        {
            count++;
            if(count == 5)
            {
				b[j] = a[i];
				b[j+1] = 0;
				i++;
				j= j+2;
				count = 0;

			}
			else
			{
				b[j] = a[i];
				i++;
				j++;
			}
        }
        else
        {
            count=0;
            b[j] = a[i];
            i++;
            j++;
        }

    }
    printf("After bit stuffing : ");
    for(i=0; i<j; i++)
    {
        printf("%d ",b[i]);
    }
    printf("\n");

    s = 0;
    p = 0;
    count = 0;

    while(s<j)
    {
        if(b[s]==1)
        {
            count++;
            if(count == 5 )
            {
				c[p] = b[s];
				p++;
				s = s+2;
				count = 0;


			}
			else
			{
				c[p] = b[s];
				p++;
				s++;
			}
        }
        else
        {
            count=0;
            c[p] = b[s];
            p++;
            s++;
        }
    }

    printf("After bit de-stuffing : ");

    for(s=0; s<p; s++)
    {
        printf("%d ",c[s]);
    }
return 0;
}
