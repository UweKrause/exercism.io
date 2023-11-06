defmodule KitchenCalculator do
  def get_volume({_unit, volume}), do: volume

  #  Unit to convert     volume   in milliliters (mL)
  #    mL                   1	             1
  #    US cup  	            1	           240
  #    US fluid ounce	      1	            30
  #    US teaspoon	        1	             5
  #    US tablespoon	      1	            15

  def to_milliliter({:milliliter, volume}), do: {:milliliter, volume}
  def to_milliliter({:cup, volume}), do: {:milliliter, volume * 240}
  def to_milliliter({:fluid_ounce, volume}), do: {:milliliter, volume * 30}
  def to_milliliter({:teaspoon, volume}), do: {:milliliter, volume * 5}
  def to_milliliter({:tablespoon, volume}), do: {:milliliter, volume * 15}

  def from_milliliter(ml, :milliliter), do: ml
  def from_milliliter({:milliliter, volume}, :cup), do: {:cup, volume / 240}
  def from_milliliter({:milliliter, volume}, :fluid_ounce), do: {:fluid_ounce, volume / 30}
  def from_milliliter({:milliliter, volume}, :teaspoon), do: {:teaspoon, volume / 5}
  def from_milliliter({:milliliter, volume}, :tablespoon), do: {:tablespoon, volume / 15}

  def convert({from_unit, from_volume}, to_unit) do
    to_milliliter({from_unit, from_volume})
    |> from_milliliter(to_unit)
  end
end
