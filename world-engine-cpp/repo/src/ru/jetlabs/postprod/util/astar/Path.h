#pragma once
#include <vector>

#include "Node.h"


/**
 * @brief
 * en
 * 
 * The Path class stores the path as a sequence of nodes.
 * Owns the nodes itself and automatically deletes them upon destruction.
 * Supports only moving, copying is prohibited.
 *
 * ru
 * 
 * Класс Path хранит путь в виде последовательности узлов.
 * Сам владеет узлами (Node) и автоматически удаляет их при уничтожении.
 * Поддерживает только перемещение, копирование запрещено.
 */
class Path {
private:
    std::vector<Node*> nodes;
    float totalCost;

public:
    explicit Path(const std::vector<Node*>& nodes, const float totalCost) {
        this->nodes = nodes;
        this->totalCost = totalCost;
    }

    std::vector<Node*> getNodes() {
        return this->nodes;
    }

    float getTotalMovementCost() const {
        return this->totalCost;
    }

    Path(const Path&) = delete;
    Path operator=(const Path&) = delete;

    Path(Path&& other) noexcept :
        nodes(std::move(other.nodes)),
        totalCost(other.totalCost) {
    }

    Path& operator=(Path&& other) noexcept {
        if (this != &other) {
            for (const Node* node : nodes) {
                delete(node);
            }

            nodes = std::move(other.nodes);
            totalCost = other.totalCost;
        }
        return *this;
    }

    ~Path() {
        for (const Node* node : nodes) {
            delete(node);
        }
    }
};
