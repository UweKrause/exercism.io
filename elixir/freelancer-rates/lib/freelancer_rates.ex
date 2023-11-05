defmodule FreelancerRates do
  @hours_in_a_day 8
  @billable_days_in_a_month 22

  def daily_rate(hourly_rate) do
    # multiplying by 1.0 ensures result is float
    hourly_rate *
      (@hours_in_a_day * 1.0)
  end

  def apply_discount(before_discount, discount) do
    before_discount -
      before_discount / 100 * discount
  end

  def monthly_rate(hourly_rate, discount) do
    (daily_rate(hourly_rate) * @billable_days_in_a_month)
    |> apply_discount(discount)
    |> Float.ceil()
    |> Kernel.trunc()
  end

  def days_in_budget(budget, hourly_rate, discount) do
    cost_per_day =
      daily_rate(hourly_rate)
      |> apply_discount(discount)

    days_in_budget = budget / cost_per_day

    Float.floor(days_in_budget, 1)
  end
end
