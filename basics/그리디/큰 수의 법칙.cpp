# include <vector>

using namespace std;

int n, m, k;
vector<int> nums;
int result;

int main() {
    cin >> n >> m >> k;

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        nums.push_back(x);
    }

    sort(nums.begin(), nums.end());
    int first = nums[n - 1];
    int second = nums[n - 2];
    int remainder = m % (k + 1);

    if (first == second)
      result = first * m;
    else
      result = first * k + second;
      result *= m / (k + 1);
      if (remainder)
        result += first * remainder;

    cout << result << endl;
}
