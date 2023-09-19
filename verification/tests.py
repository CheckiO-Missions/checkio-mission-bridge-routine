"""
TESTS is a dict with all of your tests.
Keys for this will be the categories" names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it"s used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[("four", "spades"), ("five", "spades"), ("ten", "hearts"), ("six", "hearts"), ("queen", "hearts"), ("jack", "hearts"), ("four", "hearts"), ("two", "hearts"), ("three", "diamonds"), ("seven", "diamonds"), ("four", "diamonds"), ("two", "diamonds"), ("four", "clubs")], "diamonds"],
            "answer": [8, "xx QJxxxx xxxx x"],
        },
        {
            "input": [[("three", "spades"), ("queen", "hearts"), ("jack", "hearts"), ("eight", "hearts"), ("six", "diamonds"), ("nine", "diamonds"), ("jack", "diamonds"), ("ace", "diamonds"), ("nine", "clubs"), ("king", "clubs"), ("jack", "clubs"), ("five",   "clubs"), ("ace", "clubs")], "clubs"],
            "answer": [20, "x QJx AJxx AKJxx"],
        },
        {
            "input": [[("three", "spades"), ("queen", "hearts"), ("jack", "hearts"), ("eight", "hearts"), ("six", "diamonds"), ("nine", "diamonds"), ("jack", "diamonds"), ("ace", "diamonds"), ("nine", "clubs"), ("king", "clubs"), ("jack", "clubs"), ("five", "clubs"), ("ace", "clubs")], "spades"],
            "answer": [17, "x QJx AJxx AKJxx"],
        },
    ],
    "Extra": [
        {
            "input": [[("three", "spades"), ("seven", "spades"), ("two", "spades"), ("three", "hearts"), ("queen", "hearts"), ("nine", "hearts"), ("ten", "diamonds"), ("six", "diamonds"), ("queen", "diamonds"), ("ace", "diamonds"), ("nine", "clubs"), ("four", "clubs"), ("five", "clubs")], "notrump"],
            "answer": [7, "xxx Qxx AQxx xxx"],
        },
        {
            "input": [[("ace", "spades"), ("king", "spades"), ("queen", "spades"), ("jack", "spades"), ("ten", "spades"), ("nine", "spades"), ("eight", "spades"), ("seven", "spades"), ("six", "spades"), ("five", "spades"), ("four", "spades"), ("three", "spades"), ("two", "diamonds")], "spades"],
            "answer": [26, "AKQJxxxxxxxx - x -"],
        },
        {
            "input": [[("ace", "hearts"), ("king", "spades"), ("queen", "diamonds"), ("jack", "clubs"), ("ten", "hearts"), ("nine", "spades"), ("eight", "diamonds"), ("seven", "clubs"), ("six", "hearts"), ("five", "spades"), ("four", "diamonds"), ("three", "clubs"), ("two", "hearts")], "notrump"],
            "answer": [9, "Kxx Axxx Qxx Jxx"],
        },
        {
            "input": [[("king", "hearts"), ("queen", "spades"), ("jack", "diamonds"), ("ten", "clubs"), ("nine", "clubs"), ("eight", "clubs"), ("seven", "diamonds"), ("six", "clubs"), ("five", "hearts"), ("four", "spades"), ("three", "diamonds"), ("two", "clubs"), ("ace", "hearts")], "spades"],
            "answer": [11, "Qx AKx Jxx xxxxx"],
        },
        {
            "input": [[("jack", "spades"), ("ten", "hearts"), ("nine", "clubs"), ("eight", "diamonds"), ("seven", "spades"), ("six", "hearts"), ("five", "clubs"), ("four", "diamonds"), ("three", "spades"), ("two", "spades"), ("ace", "clubs"), ("king", "diamonds"), ("queen", "spades")], "clubs"],
            "answer": [11, "QJxxx xx Kxx Axx"],
        },
    ]
}
