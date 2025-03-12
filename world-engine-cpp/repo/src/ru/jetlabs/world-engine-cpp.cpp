#include <iostream>

#include "postprod/util/astar/PathFinder.h"
#include "test/postprod/util/numpysurrogate/arrays_tests.h"
using namespace std;

bool equal_paths(const std::vector<std::pair<int, int>>& expected,
                 const std::vector<std::pair<int, int>>& actual) {
    cout<< expected.size() << " " << actual.size() << "\n";
    if (expected.size() != actual.size()) {
        return false;
    }
    for (size_t i = 0; i < expected.size(); ++i) {
        if (expected[i].first != actual[i].first || expected[i].second != actual[i].second) {
            return false;
        }
    }
    return true;
}


int main() {
    //runTestsFindIndexOfValueInVector();


    std::vector<std::vector<float>> test_map(5000, std::vector<float>(5000, 0.0f));
    std::vector<float> line(20, 1.0f);
    test_map[10] = line;
    test_map[10][18] = 0.0f;

    
    std::vector<std::pair<int, int>> path_data = {
        {0, 1}, {0, 2}, {0, 3}, {0, 4}, {0, 5}, {0, 6}, {0, 7}, {0, 8}, {0, 9},
        {1, 9}, {2, 9}, {3, 9}, {4, 9}, {5, 9}, {6, 9}, {7, 9}, {8, 9}, {9, 9},
        {10, 9}, {11, 9}, {12, 9}, {13, 9}, {14, 9}, {15, 9}, {16, 9}, {17, 9},
        {18, 9}, {18, 10}, {18, 11}, {18, 12}, {18, 13}, {18, 14}, {18, 15},
        {18, 16}, {18, 17}, {18, 18}, {18, 19}, {19, 19}
    };

    
    for (int i = 0; i < 1; ++i) {
        std::vector<std::pair<int, int>> shortest_path = PathFinder::find(test_map, {0, 0}, {19, 19});
    }
    
    //cout << equal_paths(shortest_path, path_data) << "\n";
    //cout << shortest_path.empty() << "\n";
    //cout <<"equals "<< (new SQLocation(10,10) == new SQLocation (10,10))<<"\n";
    //for (auto e : shortest_path) {
    //    cout << "{" << e.first << ", " << e.second << "}";
    //}
}
