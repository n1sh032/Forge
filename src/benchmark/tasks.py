BENCHMARK_TASKS = [
    {
        "name": "string_reverse",
        "task": """
Create a Python program called main.py.

The program should:
1. Ask the user to enter a string.
2. Print the string reversed.

Example:
Input:
hello

Output:
olleh
""",
        "tests": [
            {
                "input": "hello\n",
                "expected_output": "olleh"
            },
            {
                "input": "FORGE\n",
                "expected_output": "EGROF"
            }
        ]
    },

    {
        "name": "calculator",
        "task": """
Create a Python program called main.py.

The program should:
1. Ask the user for two numbers.
2. Print their sum.

Example:
Input:
5
7

Output:
12
""",
        "tests": [
            {
                "input": "5\n7\n",
                "expected_output": "12"
            },
            {
                "input": "10\n25\n",
                "expected_output": "35"
            }
        ]
    },

    {
        "name": "even_odd",
        "task": """
Create a Python program called main.py.

The program should:
1. Ask the user for an integer.
2. Print "Even" if the number is even.
3. Print "Odd" if the number is odd.
""",
        "tests": [
            {
                "input": "4\n",
                "expected_output": "Even"
            },
            {
                "input": "7\n",
                "expected_output": "Odd"
            }
        ]
    }
]