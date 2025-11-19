from scipy.optimize import linprog

p_a, p_b = map(int, input("Enter profit A, B (space-separated): ").split())
milk, choco = map(int, input("Enter total Milk, Choco (space-separated): ").split())
m_a, c_a = map(int, input("Enter Milk, Choco per A (space-separated): ").split())
m_b, c_b = map(int, input("Enter Milk, Choco per B (space-separated): ").split())

c = [-p_a, -p_b]
A_ub = [[m_a, m_b], [c_a, c_b]]
b_ub = [milk, choco]
bounds = [(0, None), (0, None)]

result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

if result.success:
    x, y = result.x
    profit = -result.fun
    print(f"Optimal Production:")
    print(f"Units of A: {int(x)}")
    print(f"Units of B: {int(y)}")
    print(f"Maximum Profit: Rs {int(profit)}")
else:
    print("Optimization failed")
