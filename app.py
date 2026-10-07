from grade_utils import average, passed_count


def load_scores(filename="scores.txt"):
    with open(filename, "r", encoding="utf-8") as file:
        return [int(line.strip()) for line in file if line.strip()]


def main():
    scores = load_scores()
    print("成績統計")
    print(f"人數: {len(scores)}")
    print(f"平均: {average(scores):.1f}")
    print(f"及格人數: {passed_count(scores)}")


if __name__ == "__main__":
    main()
