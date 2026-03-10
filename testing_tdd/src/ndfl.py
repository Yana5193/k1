def calculate_tax(income):
    tiers = [
        (0.,0.,0.13),
        (2_400_000,312_000,0.15),
        (5_000_000,702_000,0.18),
        (20_000_000,3_402_000,0.20),
        (50_000_000,9_402_000,0.22),
    ]
    for start, addition, taxrate in tiers[::-1]:
        if income > start:
            return addition + (income - start) * taxrate
    return

    if income < 2_400_000:
        return income * 0.13
    elif income < 5_000_000:
        return (
            2_400_000 * 0.13 +
            (income - 2_400_000) * 0.15
        )
    elif income < 20_000_000:
        return (
            2_400_000 * 0.13 +
            2_600_000 * 0.15 +
            (income - 5_000_000) * 0.18
        )
    elif income < 50_000_000:
        return (
            2_400_000 * 0.13 +
            2_600_000 * 0.15 +
            15_000_000 * 0.18 +
            (income - 20_000_000) * 0.20
        )
    elif income > 50_000_000:
        return (
            2_400_000 * 0.13 +
            2_600_000 * 0.15 +
            15_000_000 * 0.18 +
            30_000_000 * 0.20 +
            (income - 50_000_000) * 0.22
        )
