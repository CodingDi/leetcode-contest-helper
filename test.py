import unittest
from typing import Union

from main import Problem, parse_problem, ProblemSignature, FunctionSignature, Example, InteractiveProblemSignature, \
    InteractiveExample, generate_code


class ParseTest(unittest.TestCase):
    def _function_equal(self, parsed_function: FunctionSignature, function: FunctionSignature):
        assert parsed_function.return_type == function.return_type
        assert parsed_function.name == function.name
        assert parsed_function.arguments == function.arguments

    def _test_parse_problem(self, problem: Problem, signature: Union[ProblemSignature, InteractiveProblemSignature]):
        parsed_signature = parse_problem(problem)
        assert type(parsed_signature) is type(signature)
        if isinstance(signature, InteractiveProblemSignature):
            assert parsed_signature.class_name == signature.class_name
            for parsed_function, function in zip(parsed_signature.functions, signature.functions):
                self._function_equal(parsed_function, function)
        else:
            self._function_equal(parsed_signature.function, signature.function)

        assert len(parsed_signature.examples) == len(signature.examples)
        for idx in range(len(parsed_signature.examples)):
            if isinstance(signature, InteractiveProblemSignature):
                for parsed_example, example in zip(parsed_signature.examples[idx], signature.examples[idx]):
                    assert parsed_example.function == example.function
                    assert parsed_example.input == example.input
                    assert parsed_example.output == example.output
            else:
                assert parsed_signature.examples[idx].input == signature.examples[idx].input
                assert parsed_signature.examples[idx].output == signature.examples[idx].output

        solution_code, test_code = generate_code(problem, signature)
        print(solution_code)
        print(test_code)

    def test_parse_problem_1(self):
        problem = Problem(
            url="", name="Shift 2D Grid", statement="",
            examples=[
                ('Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1\n'
                 'Output: [[9,1,2],[3,4,5],[6,7,8]]'),
                ('Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4\n'
                 'Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]'),
                ('Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9\n'
                 'Output: [[1,2,3],[4,5,6],[7,8,9]]')],
            code=[
                'class Solution {',
                'public:',
                '    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {',
                '        ',
                '    }',
                '};',
            ])
        signature = ProblemSignature(
            function=FunctionSignature(
                return_type="vector<vector<int>>", name="shiftGrid",
                arguments=[("vector<vector<int>>&", "grid"), ("int", "k")]),
            examples=[
                Example(
                    {"grid": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                     "k": 1},
                    [[9, 1, 2], [3, 4, 5], [6, 7, 8]]),
                Example(
                    {"grid": [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]],
                     "k": 4},
                    [[12, 0, 21, 13], [3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10]]),
                Example(
                    {"grid": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                     "k": 9},
                    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            ])
        self._test_parse_problem(problem, signature)

    def test_parse_problem_2(self):
        problem = Problem(
            url="", name="Find Elements in a Contaminated Binary Tree", statement="",
            examples=[
                ('Input\n'
                 '["FindElements","find","find"]\n'
                 '[[[-1,null,-1]],[1],[2]]\n'
                 'Output\n'
                 '[null,false,true]\n'
                 'Explanation\n'
                 'FindElements findElements = new FindElements([-1,null,-1]); \n'
                 'findElements.find(1); // return False \n'
                 'findElements.find(2); // return True '),
                ('Input\n'
                 '["FindElements","find","find","find"]\n'
                 '[[[-1,-1,-1,-1,-1]],[1],[3],[5]]\n'
                 'Output\n'
                 '[null,true,true,false]\n'
                 'Explanation\n'
                 'FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);\n'
                 'findElements.find(1); // return True\n'
                 'findElements.find(3); // return True\n'
                 'findElements.find(5); // return False'),
                ('Input\n'
                 '["FindElements","find","find","find","find"]\n'
                 '[[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]\n'
                 'Output\n'
                 '[null,true,false,false,true]\n'
                 'Explanation\n'
                 'FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);\n'
                 'findElements.find(2); // return True\n'
                 'findElements.find(3); // return False\n'
                 'findElements.find(4); // return False\n'
                 'findElements.find(5); // return True')],
            code=[
                '/**',
                ' * Definition for a binary tree node.',
                ' * struct TreeNode {',
                ' *     int val;',
                ' *     TreeNode *left;',
                ' *     TreeNode *right;',
                ' *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}',
                ' * };',
                ' */',
                'class FindElements {',
                'public:',
                '    FindElements(TreeNode* root) {',
                '        ',
                '    }',
                '    ',
                '    bool find(int target) {',
                '        ',
                '    }',
                '};',
                '',
                '/**',
                ' * Your FindElements object will be instantiated and called as such:',
                ' * FindElements* obj = new FindElements(root);',
                ' * bool param_1 = obj->find(target);',
                ' */',
            ])
        signature = InteractiveProblemSignature(
            class_name="FindElements",
            functions=[
                FunctionSignature(
                    return_type="", name="FindElements",
                    arguments=[("TreeNode*", "root")]),
                FunctionSignature(
                    return_type="bool", name="find",
                    arguments=[("int", "target")])],
            examples=[
                [
                    InteractiveExample(
                        function="FindElements",
                        input={"root": [-1, None, -1]}, output=None),
                    InteractiveExample(
                        function="find", input={"target": 1}, output=False),
                    InteractiveExample(
                        function="find", input={"target": 2}, output=True),
                ],
                [
                    InteractiveExample(
                        function="FindElements",
                        input={"root": [-1, -1, -1, -1, -1]}, output=None),
                    InteractiveExample(
                        function="find", input={"target": 1}, output=True),
                    InteractiveExample(
                        function="find", input={"target": 3}, output=True),
                    InteractiveExample(
                        function="find", input={"target": 5}, output=False),
                ],
                [
                    InteractiveExample(
                        function="FindElements",
                        input={"root": [-1, None, -1, -1, None, -1]}, output=None),
                    InteractiveExample(
                        function="find", input={"target": 2}, output=True),
                    InteractiveExample(
                        function="find", input={"target": 3}, output=False),
                    InteractiveExample(
                        function="find", input={"target": 4}, output=False),
                    InteractiveExample(
                        function="find", input={"target": 5}, output=True),
                ],
            ]
        )
        self._test_parse_problem(problem, signature)

    def test_parse_problem_3(self):
        problem = Problem(
            url="", name="Greatest Sum Divisible by Three", statement="",
            examples=[
                ('Input: nums = [3,6,5,1,8]\n'
                 'Output: 18\n'
                 'Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).'),
                ('Input: nums = [4]\n'
                 'Output: 0\n'
                 'Explanation: Since 4 is not divisible by 3, do not pick any number.'),
                ('Input: nums = [1,2,3,4,4]\n'
                 'Output: 12\n'
                 'Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).')],
            code=[
                'class Solution {',
                'public:',
                '    int maxSumDivThree(vector<int>& nums) {',
                '        ',
                '    }',
                '};',
            ])
        signature = ProblemSignature(
            function=FunctionSignature(
                return_type="int", name="maxSumDivThree",
                arguments=[("vector<int>&", "nums")],
            ),
            examples=[
                Example(
                    {"nums": [3, 6, 5, 1, 8]},
                    18),
                Example(
                    {"nums": [4]},
                    0),
                Example(
                    {"nums": [1, 2, 3, 4, 4]},
                    12),
            ])
        self._test_parse_problem(problem, signature)

    def test_parse_problem_4(self):
        problem = Problem(
            url="", name="Minimum Moves to Move a Box to Their Target Location", statement="",
            examples=[
                ('Input: grid = [["#","#","#","#","#","#"],\n'
                 '               ["#","T","#","#","#","#"],\n'
                 '               ["#",".",".","B",".","#"],\n'
                 '               ["#",".","#","#",".","#"],\n'
                 '               ["#",".",".",".","S","#"],\n'
                 '               ["#","#","#","#","#","#"]]\n'
                 'Output: 3\n'
                 'Explanation: We return only the number of times the box is pushed.'),
                ('Input: grid = [["#","#","#","#","#","#"],\n'
                 '               ["#","T","#","#","#","#"],\n'
                 '               ["#",".",".","B",".","#"],\n'
                 '               ["#","#","#","#",".","#"],\n'
                 '               ["#",".",".",".","S","#"],\n'
                 '               ["#","#","#","#","#","#"]]\n'
                 'Output: -1'),
                ('Input: grid = [["#","#","#","#","#","#"],\n'
                 '               ["#","T",".",".","#","#"],\n'
                 '               ["#",".","#","B",".","#"],\n'
                 '               ["#",".",".",".",".","#"],\n'
                 '               ["#",".",".",".","S","#"],\n'
                 '               ["#","#","#","#","#","#"]]\n'
                 'Output: 5\n'
                 'Explanation:  push the box down, left, left, up and up.'),
                ('Input: grid = [["#","#","#","#","#","#","#"],\n'
                 '               ["#","S","#",".","B","T","#"],\n'
                 '               ["#","#","#","#","#","#","#"]]\n'
                 'Output: -1')],
            code=[
                'class Solution {',
                'public:',
                '    int minPushBox(vector<vector<char>>& grid) {',
                '        ',
                '    }',
                '};',
            ])
        signature = ProblemSignature(
            function=FunctionSignature(
                return_type="int", name="minPushBox",
                arguments=[("vector<vector<char>>&", "grid")],
            ),
            examples=[
                Example(
                    {"grid": [["#", "#", "#", "#", "#", "#"],
                              ["#", "T", "#", "#", "#", "#"],
                              ["#", ".", ".", "B", ".", "#"],
                              ["#", ".", "#", "#", ".", "#"],
                              ["#", ".", ".", ".", "S", "#"],
                              ["#", "#", "#", "#", "#", "#"]]},
                    3),
                Example(
                    {"grid": [["#", "#", "#", "#", "#", "#"],
                              ["#", "T", "#", "#", "#", "#"],
                              ["#", ".", ".", "B", ".", "#"],
                              ["#", "#", "#", "#", ".", "#"],
                              ["#", ".", ".", ".", "S", "#"],
                              ["#", "#", "#", "#", "#", "#"]]},
                    -1),
                Example(
                    {"grid": [["#", "#", "#", "#", "#", "#"],
                              ["#", "T", ".", ".", "#", "#"],
                              ["#", ".", "#", "B", ".", "#"],
                              ["#", ".", ".", ".", ".", "#"],
                              ["#", ".", ".", ".", "S", "#"],
                              ["#", "#", "#", "#", "#", "#"]]},
                    5),
                Example(
                    {"grid": [["#", "#", "#", "#", "#", "#", "#"],
                              ["#", "S", "#", ".", "B", "T", "#"],
                              ["#", "#", "#", "#", "#", "#", "#"]]},
                    -1),
            ])
        self._test_parse_problem(problem, signature)
