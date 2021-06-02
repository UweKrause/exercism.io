defmodule WordCount do
  @doc """
  Count the number of words in the sentence.

  Words are compared case-insensitively.
  """
  @spec count(String.t()) :: map
  def count(sentence) do
    words = Regex.scan(~r/[1-9a-zA-ZßäöüÄÖÜ-]{1,}/u, sentence)
    count(words, %{})
  end

  def count([[word] | words_remaining], result) do
    key = String.downcase(word)
    value = Map.get(result, key, 0)
    {_, result} = Map.get_and_update(result, key, fn current -> {current, value + 1} end)

    count(words_remaining, result)
  end

  def count([], result) do
    result
  end

end
