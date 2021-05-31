defmodule RotationalCipher do
  @doc """
  Given a plaintext and amount to shift by, return a rotated string.

  Example:
  iex> RotationalCipher.rotate("Attack at dawn", 13)
  "Nggnpx ng qnja"
  """
  @spec rotate(text :: String.t(), shift :: integer) :: String.t()
  def rotate(text, shift) do
    String.to_charlist(text)
    |> Enum.map(&rotate_character(&1, shift))
    |> List.to_string
  end

  defp rotate_character(letter, shift) when (letter >= ?A) and (letter <= ?Z) do
    first = ?A
    last = ?Z
    rotate_character(letter, shift, first, last)
  end

  defp rotate_character(letter, shift) when (letter >= ?a) and (letter <= ?z) do
    first = ?a
    last = ?z
    rotate_character(letter, shift, first, last)
  end

  defp rotate_character(letter, _shift) do
    # Character is not alphabetical, just return it without changes
    letter
  end

  defp rotate_character(letter, shift, first, last) do
    alphabet = Enum.to_list(first..last)
    position_in_alphabet = rem((letter - first + shift), length(alphabet))
    Enum.at(alphabet, position_in_alphabet)
  end

end
