#include <string>

using namespace std;

string now;
int result = 0;
int dx[] = {-2, -2, -1, -1, 1, 1, 2, 2};
int dy[] = {-1, 1, -2, 2, -2, 2, -1, 1};

int main(){
  cin >> now;
  int row = now[1] - '0'; // '1'은 49
  int col = now[0] - 'a' + 1;

  for(int i = 0; i < 8; i++){
    int nrow = row + dx[i];
    int ncol = col + dy[i];

    if(nrow > 0 && nrow < 9 && ncol > 0 && ncol < 9)
      result++;
  }

  cout << result << '\n';
}
