using namespace std;

int n = 1260;
int k = 0;
int coins[4] = {500, 100, 50, 10}

int main(){
  for(int i; i < 4; i++){
    k = n / coins[i]
    n %= coins[i]
  }
  cout << k << '\n';

}
