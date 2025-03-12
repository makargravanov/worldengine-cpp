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
        const float movementCost = mapData[(y * width) + x];
        return new Node(location, movementCost, (y * width) + x);
    }

    Node* handleNode(const int x, const int y, Node* fromNode, const int destinationX, const int destinationY) const {
        Node* n = getNode(new SQLocation(x, y));
        if (n != nullptr) {
            const int dx = std::max(x, destinationX) - std::min(x, destinationX);
            const int dy = std::max(y, destinationY) - std::min(y, destinationY);
            const float emCost = static_cast<float>(dx + dy);
            n->setMovementCost(n->getMovementCost() + fromNode->getMovementCost());
            n->setScore(n->getMovementCost() + emCost);
            n->setParent(fromNode);
            return n;
        }
        return nullptr;
    }

    std::vector<Node*> getAdjacentNodes(Node* currentNode, const SQLocation* destination) const {
        std::vector<Node*> result = {};

        const SQLocation* cL = currentNode->getLocation();
        Node* n = handleNode(cL->x() + 1, cL->y(), currentNode, destination->x(), destination->y());
        if (n != nullptr) {
            result.push_back(n);
        }
        n = handleNode(cL->x() - 1, cL->y(), currentNode, destination->x(), destination->y());
        if (n != nullptr) {
            result.push_back(n);
        }
        n = handleNode(cL->x(), cL->y() + 1, currentNode, destination->x(), destination->y());
        if (n != nullptr) {
            result.push_back(n);
        }
        n = handleNode(cL->x(), cL->y() - 1, currentNode, destination->x(), destination->y());
        if (n != nullptr) {
            result.push_back(n);
        }
        return result;
    }


    /*
    * def get_adjacent_nodes(self, cur_node, destination):
        result = []

        cl = cur_node.location
        dl = destination

        n = self._handle_node(cl.x + 1, cl.y, cur_node, dl.x, dl.y)
        if n:
            result.append(n)
        n = self._handle_node(cl.x - 1, cl.y, cur_node, dl.x, dl.y)
        if n:
            result.append(n)
        n = self._handle_node(cl.x, cl.y + 1, cur_node, dl.x, dl.y)
        if n:
            result.append(n)
        n = self._handle_node(cl.x, cl.y - 1, cur_node, dl.x, dl.y)
        if n:
            result.append(n)

        return result

     */
};
