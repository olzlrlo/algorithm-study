using namespace std;

int n, m;
int result = 0;

int main(){
  cin >> n >> m;

   for (int i = 0; i < n; i++) {
     for (int j = 0; j < m; j++) {
        int x;
        cin >> x;
        min_val = min(min_val, x);
      }
      result = max(result, min_val);
   }
   cout << result << '\n';
}
