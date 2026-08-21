"""
test for analyzer/tree_view.py(JSONTreeGenerator)
"""
import pytest
from analyzer.tree_view import JSONTreeGenerator

@pytest.fixture
def generator():
    return JSONTreeGenerator()


def test_generate_tree_prints_dict_of_primitives_in_order(generator,capsys):
    #generator = JSONTreeGenerator()
    data = {"c": 3, "b": 2, "a": 1}

    generator.generate_tree(data)

    captured = capsys.readouterr()
    expected = (
        ".\n"
        "├── c: 3\n"
        "├── b: 2\n"
        "└── a: 1\n"
    )
    assert captured.out == expected

def test_generate_tree_prints_dict_of_nested_in_order(generator,capsys):
    employees = {
        "emp1": {"name": "Alice", "role": "Developer"},
        "emp2": {"name": "Bob", "role": "Designer"}
    }
    generator.generate_tree(employees)

    captured = capsys.readouterr()
    expected = (
        ".\n"
        "├── emp1\n"
        "│   ├── name: Alice\n"
        "│   └── role: Developer\n"
        "└── emp2\n"
        "    ├── name: Bob\n"
        "    └── role: Designer\n"
    )
    assert captured.out == expected

def test_generate_tree_prints_list_of_primitive_in_order(generator,capsys):
    primitives_list = ["Alice", 42, "Developer", True]

    generator.generate_tree(primitives_list)

    captured = capsys.readouterr()
    expected = (
        ".\n"
        "├── [0]: Alice\n"
        "├── [1]: 42\n"
        "├── [2]: Developer\n"
        "└── [3]: True\n"
    )
    assert captured.out == expected

def test_generate_tree_prints_list_with_nested_list_or_dict_in_order(generator,capsys):
    mixed_list = [
        "Project A",
        ["Task 1", "Task 2"],
        {"status": "Active", "priority": "High"}
    ]
    generator.generate_tree(mixed_list)

    captured = capsys.readouterr()
    expected = (
        ".\n"
        "├── [0]: Project A\n"
        "├── [1]\n"
        "│   ├── [0]: Task 1\n"
        "│   └── [1]: Task 2\n"
        "└── [2]\n"
        "    ├── status: Active\n"
        "    └── priority: High\n"
    )
    assert captured.out == expected



