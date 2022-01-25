#include <string>

using namespace std;

int n, result;

bool check(int h, int m, int s){
  if (h % 10 == 3 || m / 10 == 3 || m % 10 == 3 || s / 10 == 3 || s % 10 == 3)
    return true;
  else
    return false;
}

int main(){
  cin >> n;
  for (int h = 0; h <= n; h++){
    for (int m = 0; m < 60; m++){
      for (int s = 0; s < 60; s++){
        if (check(h, m, s))
          result++;
      }
    }
  }
  cout << cnt << '\n';
}
