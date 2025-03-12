#pragma once
#include "SQLocation.h"

class Node {
private:
    SQLocation* location;
    float movementCost;
    Node* parent;
    float score;
    int locationId;

public:
    Node(SQLocation* location, const float movementCost, const int locationId, Node* parent = nullptr) {
        this->location = location;
        this->movementCost = movementCost;
        this->parent = parent;
        this->score = 0;
        this->locationId = locationId;
    }

    SQLocation* getLocation() const {
        return location;
    }

    float getMovementCost() const {
        return movementCost;
    }

    Node* getParent() const {
        return parent;
    }

    float getScore() const {
        return score;
    }

    int getLocationId() const {
        return locationId;
    }

    void setLocation(SQLocation* loc) {
        this->location = loc;
    }

    void setMovementCost(const float mCost) {
        this->movementCost = mCost;
    }

    void setParent(Node* par) {
        this->parent = par;
    }

    void setScore(const float sc) {
        this->score = sc;
    }

    void setLocationId(const int lId) {
        this->locationId = lId;
    }

    bool operator==(const Node& other) const {
        return other.getLocationId() == locationId;
    }

    Node(const Node&) = delete;
    Node& operator=(const Node&) = delete;

    Node(Node&& other) noexcept :
        location(other.location),
        movementCost(other.movementCost),
        parent(other.parent),
        score(other.score),
        locationId(other.locationId) {
        other.location = nullptr;
    }

    Node& operator=(Node&& other) noexcept {
        if (this != &other) {
            delete location;

            location = other.location;
            movementCost = other.movementCost;
            parent = other.parent;
            score = other.score;
            locationId = other.locationId;

            other.location = nullptr;
        }
        return *this;
    }

    ~Node() {
        delete(location);
    }
};
