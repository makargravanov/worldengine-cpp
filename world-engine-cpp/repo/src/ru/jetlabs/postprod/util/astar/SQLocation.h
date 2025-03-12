#pragma once

class SQLocation {
private:
    int coordX, coordY;

public:
    explicit SQLocation(const int x, const int y) {
        coordX = x;
        coordY = y;
    }

    int x() const {
        return coordX;
    }

    int y() const {
        return coordY;
    }

    bool operator==(const SQLocation& o) const {
        return coordX == o.coordX && coordY == o.coordY;
    }
};
