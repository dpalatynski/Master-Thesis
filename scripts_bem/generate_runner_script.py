import random


def main():
    #  choosing proper parameters, different for each unleash.sh file
    hs = [0.25, 0.75]
    ps = [0.15, 0.2, 0.3, 0.35, 0.4, 0.45]
    a, b, c, d = 0.25, 0.25, 0.25, 0.25
    q = 4
    result = []

    for h in hs:
        for p in ps:
            command = f'qsub -v p={p},q={q},a={a},b={b},c={c},d={d},h={h} simulation.sh \n'
            result.append(command)
    random.shuffle(result)
    with open("unleash.sh", "w") as handle:
        handle.writelines(result)


if __name__ == "__main__":
    main()
