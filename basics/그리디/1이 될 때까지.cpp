using namespace std;

int n, k;
int result = 0;

int main() {
    cin >> n >> k;

    while (n >= k) {
      int remainder = n % k;
      if (remainder){
        n -= remainder;
        result += remainder;
      }
      n /= k;
      result += 1;
    }

    result += (n - 1);
    cout << result << '\n';
}
