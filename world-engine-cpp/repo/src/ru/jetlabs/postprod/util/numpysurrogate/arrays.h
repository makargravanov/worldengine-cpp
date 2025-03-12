#pragma once

#include <vector>
template <typename T>
std::vector<T> flattenMatrix(const std::vector<std::vector<T>>& matrix) {
    std::vector<T> flattened;
    
    size_t total_size = 0;
    for (const auto& row : matrix) {
        total_size += row.size();
    }
    flattened.reserve(total_size);
    
    for (const auto& row : matrix) {
        flattened.insert(flattened.end(), row.begin(), row.end());
    }
    
    return flattened;
}

//TODO: Multi-thread search for huge arrays
template <typename T>
int64_t findIndexOfValueInVector(const T* value, std::vector<T*>& in) {
    auto it = std::find(in.begin(), in.end(), value);
    if (it != in.end()) {
        return std::distance(in.begin(), it);
    } else {
        return -1;
    }
}

template <typename T>
int64_t findIndexOfValueInVector(const T value, std::vector<T>& in) {
    auto it = std::find(in.begin(), in.end(), value);
    if (it != in.end()) {
        return std::distance(in.begin(), it);
    } else {
        return -1;
    }
}