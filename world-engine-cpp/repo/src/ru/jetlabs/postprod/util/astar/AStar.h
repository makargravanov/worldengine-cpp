#pragma once

#include "AStarMemoryManager.h"
#include "Path.h"
#include "SQMapHandler.h"
#include "../numpysurrogate/arrays.h"

class AStar {
    SQMapHandler* mapHandler;
    std::vector<int> openLocationIdVec;
    std::vector<Node*> openNodes;
    std::vector<int> closedLocationsIdVec;

public:
    explicit AStar(SQMapHandler* mapHandler) {
        this->mapHandler = mapHandler;
        openLocationIdVec = {};
        openNodes = {};
        closedLocationsIdVec = {};
        AStarMemoryManager::add(this);
    }
    
    Node* getBestOpenNode() const {
        Node* bestNode = nullptr;
        for (Node* n : openNodes) {
            if (bestNode == nullptr) {
                bestNode = n;
            }
            else {
                if (n->getScore() <= bestNode->getScore()) {
                    bestNode = n;
                }
            }
        }
        return bestNode;
    }

    static Path* tracePath(Node* n) {
        std::vector<Node*> nodes = {};
        const float totalCost = n->getMovementCost();
        Node* parent = n->getParent();
        nodes.push_back(n);
        
        while (true) {
            if (parent == nullptr) {
                break;
            }
            nodes.push_back(parent);
            parent = parent->getParent();
        }
      
        std::reverse(nodes.begin(), nodes.end());
        return new Path(nodes, totalCost);
    }

    Node* handleNode(Node* node, const SQLocation* end) {
        int64_t i = findIndexOfValueInVector(node->getLocationId(), openLocationIdVec);
        openNodes.erase(openNodes.begin() + i);
        openLocationIdVec.erase(openLocationIdVec.begin() + i);
        closedLocationsIdVec.push_back(node->getLocationId());

        const std::vector<Node*> nodes = mapHandler->getAdjacentNodes(node, end);

        for (Node* n : nodes) {
            if (*n->getLocation() == *end) {
                return n;
            }
            else if (findIndexOfValueInVector(n->getLocationId(), closedLocationsIdVec) != -1) {
                continue;
            }
            else if (findIndexOfValueInVector(n->getLocationId(), openLocationIdVec) != -1) {
                i = findIndexOfValueInVector(n->getLocationId(), openLocationIdVec);
                const Node* openNode = openNodes[i];
                if (n->getMovementCost() < openNode->getMovementCost()) {
                    openNodes.erase(openNodes.begin() + i);
                    openLocationIdVec.erase(openLocationIdVec.begin() + i);
                    openNodes.push_back(n);
                    openLocationIdVec.push_back(n->getLocationId());
                }
            }
            else {
                openNodes.push_back(n);
                openLocationIdVec.push_back(n->getLocationId());
            }
        }
        return nullptr;
    }

    Path* findPath(SQLocation* fromLocation, SQLocation* toLocation) {
        SQLocation* end = toLocation;
        Node* fNode = mapHandler->getNode(fromLocation);
        openNodes.push_back(fNode);
        openLocationIdVec.push_back(fNode->getLocationId());
        Node* nextNode = fNode;

        int counter = 0;
        while (nextNode != nullptr) {
            if (counter > 10000) {
                break;
            }
            Node* finish = handleNode(nextNode, end);
            if (finish != nullptr) {
                return tracePath(finish);
            }
            nextNode = getBestOpenNode();
            counter += 1;
        }

        return nullptr;
    }
};
