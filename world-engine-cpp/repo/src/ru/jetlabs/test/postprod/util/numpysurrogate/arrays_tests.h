#pragma once
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
#include "../../../../postprod/util/numpysurrogate/arrays.h"
/**
 *
 * TESTS-1: int64_t findIndexOfValueInVector(const T value, std::vector<T>& in) {};
 * 
 */

inline void runTestsFindIndexOfValueInVector() {
    std::cout << "Start of tests with findIndexOfValueInVector" << '\n';
    // Тест 1: Поиск существующего элемента
    {
        std::vector<int> vec = {1, 2, 3, 4, 5};
        int64_t index = findIndexOfValueInVector(3, vec);
        assert(index == 2); // 3 находится на индексе 2
    }

    // Тест 2: Поиск несуществующего элемента
    {
        std::vector<int> vec = {1, 2, 3, 4, 5};
        int64_t index = findIndexOfValueInVector(6, vec);
        assert(index == -1); // 6 не существует в векторе
    }

    // Тест 3: Поиск первого вхождения нескольких одинаковых элементов
    {
        std::vector<int> vec = {1, 2, 3, 2, 5};
        int64_t index = findIndexOfValueInVector(2, vec);
        assert(index == 1); // Первое вхождение 2 находится на индексе 1
    }

    // Тест 4: Пустой вектор
    {
        std::vector<int> vec = {};
        int64_t index = findIndexOfValueInVector(1, vec);
        assert(index == -1); // Пустой вектор, элемент не найден
    }

    // Тест 5: Поиск в векторе строк
    {
        std::vector<std::string> vec = {"apple", "banana", "orange"};
        int64_t index = findIndexOfValueInVector(std::string("banana"), vec);
        assert(index == 1); // "banana" находится на индексе 1
    }

    std::cout << "End of tests with findIndexOfValueInVector" << '\n';
}
