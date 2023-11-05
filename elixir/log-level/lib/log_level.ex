defmodule LogLevel do
  def to_label(0, false), do: :trace
  def to_label(1, _), do: :debug
  def to_label(2, _), do: :info
  def to_label(3, _), do: :warning
  def to_label(4, _), do: :error
  def to_label(5, false), do: :fatal
  def to_label(_level, _legacy?), do: :unknown

  def alert_recipient(level, legacy?) do
    to_label(level, legacy?)
    |> get_recipient(legacy?)
  end

  # If the log label is error or fatal, send the alert to the ops team.
  defp get_recipient(:error, _), do: :ops
  defp get_recipient(:fatal, _), do: :ops

  # If you receive a log with an unknown label from a legacy system,
  # send the alert to the dev1 team,
  defp get_recipient(:unknown, true), do: :dev1

  # other unknown labels should be sent to the dev2 team.
  defp get_recipient(:unknown, _), do: :dev2

  # All other log labels can be safely ignored by returning false.
  defp get_recipient(_, _), do: false
end
