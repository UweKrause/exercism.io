defmodule Lasagna do
  @doc """
    How many minutes the lasagna should be in the oven.
    ## Example
      iex> Lasagna.expected_minutes_in_oven()
      40
  """
  def expected_minutes_in_oven() do
    # According to the cooking book
    40
  end

  @doc """
    How many minutes the lasagna still has to remain in the oven,
    based on the expected oven time in minutes.
    ## Parameter
        - in_oven: the actual minutes the lasagna has been in the oven
    ## Example
      iex> Lasagna.remaining_minutes_in_oven(30)
      10
  """
  def remaining_minutes_in_oven(in_oven) when is_integer(in_oven) do
    expected_minutes_in_oven() - in_oven
  end

  @doc """
    How many minutes you spent preparing the lasagna.
    ## Parameter
      - layers: The number of layers you added to the lasagna
    ## Example
      iex> Lasagna.preparation_time_in_minutes(2)
      4
  """
  def preparation_time_in_minutes(layers) when is_integer(layers) do
    # assumed time each layer takes you to prepare
    minutes = 2
    layers * minutes
  end

  @doc """
    How many minutes in total you've worked on cooking the lasagna.
    ## Parameters
      - layers: the number of layers you added to the lasagna
      - in_oven: the number of minutes the lasagna has been in the oven
    ## Example
      iex> Lasagna.total_time_in_minutes(3, 20)
      26
  """
  def total_time_in_minutes(layers, in_oven) when is_integer(layers) and is_integer(in_oven) do
    preparation_time_in_minutes(layers) + in_oven
  end

  @doc """
  A message indicating that the lasagna is ready to eat.
  """
  def alarm() do
    "Ding!"
  end
end
