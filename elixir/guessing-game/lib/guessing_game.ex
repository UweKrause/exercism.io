defmodule GuessingGame do
  # 5. Make the response when there is no guess
  # Elixir: default argument must be defined early
  def compare(secret_number, guess \\ :no_guess)
  def compare(secret_number, :no_guess), do: "Make a guess"

  # 1. Make the response when the guess matches the secret number
  def compare(same, same), do: "Correct"

  # 4. Make the responses when the guess is one more or one less than the secret number
  # Elixir: Special case must be defined before more general cases
  def compare(secret_number, guess)
      when guess == secret_number - 1 or guess == secret_number + 1 do
    "So close"
  end

  # 2. Make the response when the guess is greater than the secret number
  def compare(secret_number, guess) when guess > secret_number do
    "Too high"
  end

  # 3. Make the response when the guess is less than the secret number
  def compare(secret_number, guess) when guess < secret_number do
    "Too low"
  end
end
