#include <bits/stdc++.h>
using namespace std;

int n, m;
int graph[201][201];

// 상, 하, 좌, 우
int dx[] = {0, 0, -1, 1};
int dy[] = {-1, 1, 0, 0};

int bfs(int x, int y){
  queue<pair<int, int> > q;
  q.push({x, y});

  while(!q.empty()){
    int x = q.front().first;
    int y = q.front().second;
    q.pop();

    for(int i = 0; i < 4; i++){
      int nx = x + dy[i];
      int ny = y + dy[i];

      if(nx < 0 || nx >= n || ny < 0 || ny >= n)
        continue;
      if(graph[nx][ny]==0)
        continue;
      if(graph[nx][ny]){
        graph[nx][ny] = graph[x][y] + 1;
        q.push({nx, ny});
      }
    }
  }
  return graph[n - 1][m - 1];
}

int main(void) {
  cin >> n >> m;
  for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
          scanf("%1d", &graph[i][j]);
      }
  }
  cout << bfs(0, 0) << '\n';
  return 0;
}
