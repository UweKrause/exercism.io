defmodule NucleotideCount do
  @nucleotides [?A, ?C, ?G, ?T]

  @doc """
  Counts individual nucleotides in a DNA strand.

  ## Examples

  iex> NucleotideCount.count('AATAA', ?A)
  4

  iex> NucleotideCount.count('AATAA', ?T)
  1
  """
  @spec count(charlist(), char()) :: non_neg_integer()
  def count(strand, nucleotide) do
    count(strand, nucleotide, 0)
  end

  @spec count(charlist(), char(), non_neg_integer()) :: non_neg_integer()

  defp count([], _nucleotide, count) do
    count
  end

  defp count(strand, nucleotide, count) do
    [head | tail] = strand
    count = if(head == nucleotide, do: count + 1, else: count)
    count(tail, nucleotide, count)
  end



  @doc """
  Returns a summary of counts by nucleotide.

  ## Examples

  iex> NucleotideCount.histogram('AATAA')
  %{?A => 4, ?T => 1, ?C => 0, ?G => 0}
  """
  @spec histogram(charlist()) :: map()
  def histogram(strand) do
    histogram(strand, 0, 0, 0, 0)
  end

  def histogram([], a, t, c, g) do
    %{?A => a, ?T => t, ?C => c, ?G => g}
  end

  def histogram(strand, a, t, c, g) do
    [head | tail] = strand

    a = if(head == ?A, do: a + 1, else: a)
    t = if(head == ?T, do: t + 1, else: t)
    c = if(head == ?C, do: c + 1, else: c)
    g = if(head == ?G, do: g + 1, else: g)

    histogram(tail, a, t, c, g)
  end

end
