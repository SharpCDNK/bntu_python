import tkinter as tk

def calculate_future_value():
    try:
        investment_amount = float(investment_entry.get())
        years = float(years_entry.get())
        interest_rate = float(rate_entry.get()) / 100

        future_value = investment_amount * (1 + interest_rate) ** (years*12)
        result_label.config(text=f"Future Value: ${future_value:,.2f}")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

root = tk.Tk()
root.title("Investment Calculator")

tk.Label(root, text="Investment Amount:").grid(row=0, column=0)
investment_entry = tk.Entry(root)
investment_entry.grid(row=0, column=1)

tk.Label(root, text="Years:").grid(row=1, column=0)
years_entry = tk.Entry(root)
years_entry.grid(row=1, column=1)

tk.Label(root, text="Interest Rate (%):").grid(row=2, column=0)
rate_entry = tk.Entry(root)
rate_entry.grid(row=2, column=1)

calculate_button = tk.Button(root, text="Calculate", command=calculate_future_value)
calculate_button.grid(row=3, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=2)

root.mainloop()
