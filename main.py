from get_contribution import get_contributions

def main() -> None:
    contribs = get_contributions("zawa-kun")
    for date, level in contribs[-7:]:
        print(f'{date}: {level} level')

if __name__ == '__main__':
    main()