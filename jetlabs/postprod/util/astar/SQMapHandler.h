#pragma once
#include <vector>

#include "Node.h"

class SQMapHandler {
private:
    std::vector<float> mapData;
    int width;
    int height;

public:
    SQMapHandler(const std::vector<float>& mapData, const int width, const int height) {
        this->mapData = mapData;
        this->width = width;
        this->height = height;
    }

    Node* getNode(SQLocation* location) const {
        const int x = location->x();
        const int y = location->y();
        if (x < 0 || x >= width || y >= height) {
            return nullptr;
        }
        const float movementCost = mapData[(y*width)+x];
        return new Node(location, movementCost, (y*width)+x );
    
    }
};
