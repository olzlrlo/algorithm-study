#include <string>

using namespace std;

int n;
string plans;
int x = 1, y = 1;

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};
char moves[4] = {'L', 'R', 'U', 'D'};

int main(){
  cin >> n;
  cin.ignore(); // 버퍼 비우기
  getline(cin, plans); // 이동 계획을 하나씩 확인

  for (int i = 0; i < plans.size(); i++){
    int nx, ny;
    for (int j = 0; j < 4; j++){
      if (plans[i] == moves[j]){
        nx = x + dx[j];
        ny = y + dy[j];
      }
    }
    if (nx < 1 || nx > n || ny < 1 || ny > n)
      continue;
    else
      x = nx;
      y = ny;
  }

  cout << x << ' ' << y << '\n';
  return 0;
}
