#include <string>
#include <vector>
#include <map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    map<string, int> spies;

    for(auto cloth: clothes)
        spies[cloth[1]] += 1;

    for(auto spy: spies){
        answer *= spy.second + 1;
    }
    return answer - 1;
}
