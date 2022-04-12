//
// Created by Sean Anderson on 5/13/21.
//

#ifndef FINAL_PROJECT_SANDER15_WORD_H
#define FINAL_PROJECT_SANDER15_WORD_H

#include <iomanip>
#include <fstream>
#include <string>
#include <vector>

class Word {
private:
    std::string word;
    int points;

public:
    Word() {
        word = "";
        points = 0;
    }
    Word(std::string word) {
        this->word = word;
        points = word.size() - 3;
    }

    std::string getWord() {
        return word;
    }

    int getPoints() {
        return points;
    }

};

#endif //FINAL_PROJECT_SANDER15_WORD_H
