#pragma once
#include <vector>

#include "Node.h"

class Path {
private:
    std::vector<Node*> nodes;
    float totalCost;

public:
    explicit Path(const std::vector<Node*>& nodes, const float totalCost) {
        this->nodes = nodes;
        this->totalCost = totalCost;
        AStarMemoryManager::add(this);
    }

    std::vector<Node*> getNodes() {
        return this->nodes;
    }

    float getTotalMovementCost() const {
        return this->totalCost;
    }
   
};
