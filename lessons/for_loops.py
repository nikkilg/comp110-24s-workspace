"""Practice writing for loops."""

pets: list[str] = ["Loulie", "Bo", "Bear"]

for item in pets:
    print(f"Good boy, {item}!")


"""Range in for loops."""

names: list[str] = ["Alyssa", "Vrinda", "Janet"]
for idx in range(0, len(names)):
    print(f"{idx}: {names[idx]}")