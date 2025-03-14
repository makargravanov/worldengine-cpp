#pragma once
#include <cassert>
#include <vector>

class AStar;
class Path;
class SQLocation;
class SQMapHandler;
class Node;


class AStarMemoryManager {
private:
    std::vector<SQLocation*> locations;
    std::vector<SQMapHandler*> handlers;
    std::vector<Node*> nodes;
    std::vector<Path*> pathVec;
    std::vector<AStar*> astarVec;

    static AStarMemoryManager* instance;

public:
    
    static AStarMemoryManager* init() noexcept {
        return new AStarMemoryManager();
    }


    static void add(SQLocation* pointer) noexcept {
        instance->locations.push_back(pointer);
    }

    static void add(SQMapHandler* pointer) noexcept {
        instance->handlers.push_back(pointer);
    }

    static void add(Node* pointer) noexcept {
        instance->nodes.push_back(pointer);
    }

    static void add(Path* pointer) noexcept {
        instance->pathVec.push_back(pointer);
    }

    static void add(AStar* pointer) noexcept {
        instance->astarVec.push_back(pointer);
    }

    AStarMemoryManager(const AStarMemoryManager&) = delete;
    AStarMemoryManager& operator=(const AStarMemoryManager&) = delete;
    AStarMemoryManager(AStarMemoryManager&&) = delete;
    AStarMemoryManager& operator=(AStarMemoryManager&&) = delete;

    ~AStarMemoryManager() {
        clear();
        instance = nullptr;
    }

private:
    AStarMemoryManager() {
        if (instance == nullptr) {
            locations = std::vector<SQLocation*>();
            handlers = std::vector<SQMapHandler*>();
            nodes = std::vector<Node*>();
            pathVec = std::vector<Path*>();
            astarVec = std::vector<AStar*>();
            
            instance = this;
        }
        else {
            throw std::exception();
        }
    }


    static void clear() noexcept;
};
