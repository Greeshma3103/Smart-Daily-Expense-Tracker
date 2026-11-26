#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Usage: expense.exe <monthly_budget> <total_expense>\\n");
        return 1;
    }
    double budget = atof(argv[1]);
    double total = atof(argv[2]);
    printf("%.2f %.2f %.2f", total, budget-total, budget > 0 ? (total/budget)*100 : 0);
    return 0;
}
