# ÇÖZÜM YAKLAŞIMLARI
# Mustafa'nın Algoritma Çözüm Rehberi

## KULLANIM KILAVUZU
⚠️ **UYARI**: Bu dosya sadece ihtiyaç duyulduğunda açılmalıdır!
- Önce problemi kendin çözmeye çalış
- Takıldığında bu dosyaya bak
- Çözümü gördükten sonra kendi çözümünü yaz
- Bu dosya spoiler içerir!

---

## 1. PYTHON ALGORİTMA ÇÖZÜMLERİ

### 1.3. İki Sayının Toplamı

**Problem:** Verilen bir dizide, toplamı belirli bir hedef sayıya eşit olan iki sayıyı bul.

**Brute Force Yaklaşımı (O(n²)):**
```python
def two_sum_brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
```

**Hash Table Yaklaşımı (O(n)) - ÖNERİLEN:**
```python
def two_sum_hash_table(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

**Çözüm Mantığı:**
1. Her eleman için: `target - eleman = aradığımız_sayı`
2. Hash table'da aradığımız sayı var mı kontrol et
3. Varsa çözümü buldun
4. Yoksa mevcut elemanı hash table'a ekle

**Time Complexity:** O(n)
**Space Complexity:** O(n)

---

### 1.5. Palindrom Kontrolü

**Problem:** Verilen bir dizenin palindrom olup olmadığını kontrol et.

**Two Pointer Yaklaşımı (O(n)):**
```python
def is_palindrome(s):
    # Temizleme: sadece alfanumerik karakterler
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    left, right = 0, len(cleaned) - 1
    
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    
    return True
```

**Alternatif: String Reversal (O(n)):**
```python
def is_palindrome_reverse(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]
```

**Çözüm Mantığı:**
1. String'i temizle (büyük/küçük harf, noktalama)
2. İki pointer ile baştan ve sondan karşılaştır
3. Farklı karakter bulursan False döndür

**Time Complexity:** O(n)
**Space Complexity:** O(1) (in-place)

---

### 1.7. Faktöriyel Hesaplama

**Problem:** Verilen bir sayının faktöriyelini hesapla.

**Iterative Yaklaşım (O(n)):**
```python
def factorial_iterative(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

**Recursive Yaklaşım (O(n)):**
```python
def factorial_recursive(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)
```

**Big Number Handling:**
```python
import math

def factorial_big(n):
    return math.factorial(n)
```

**Çözüm Mantığı:**
- Base case: 0! = 1, 1! = 1
- Recursive: n! = n × (n-1)!
- Iterative: 1'den n'e kadar çarp

**Time Complexity:** O(n)
**Space Complexity:** O(1) (iterative), O(n) (recursive)

---

### 1.8. Fibonacci Dizisi

**Problem:** Fibonacci dizisinin n. terimini hesapla.

**Recursive Yaklaşım (O(2^n)) - YAVAŞ:**
```python
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
```

**Iterative Yaklaşım (O(n)) - ÖNERİLEN:**
```python
def fibonacci_iterative(n):
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

**Dynamic Programming (O(n)):**
```python
def fibonacci_dp(n):
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]
```

**Çözüm Mantığı:**
- Base case: F(0) = 0, F(1) = 1
- Recurrence: F(n) = F(n-1) + F(n-2)
- İki değişken ile iteratif çözüm en verimli

**Time Complexity:** O(n)
**Space Complexity:** O(1) (iterative)

---

### 2.2. En Uzun Ortak Önek

**Problem:** Bir dizi dize içinde en uzun ortak öneki bul.

**Horizontal Scanning (O(S)):**
```python
def longest_common_prefix(strs):
    if not strs:
        return ""
    
    # İlk string'i referans al
    prefix = strs[0]
    
    for string in strs[1:]:
        # Prefix'i kısalt
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix
```

**Vertical Scanning (O(S)):**
```python
def longest_common_prefix_vertical(strs):
    if not strs:
        return ""
    
    # En kısa string'in uzunluğu kadar döngü
    for i in range(len(strs[0])):
        char = strs[0][i]
        
        # Diğer string'lerde aynı pozisyondaki karakteri kontrol et
        for string in strs[1:]:
            if i >= len(string) or string[i] != char:
                return strs[0][:i]
    
    return strs[0]
```

**Çözüm Mantığı:**
1. İlk string'i referans al
2. Diğer string'lerle karşılaştır
3. Farklı karakter bulduğunda dur
4. O ana kadar olan kısmı döndür

**Time Complexity:** O(S) (S = tüm string'lerin toplam uzunluğu)
**Space Complexity:** O(1)

---

### 2.4. Valid Parantezler

**Problem:** Bir dizedeki parantezlerin geçerli olup olmadığını kontrol et.

**Stack Yaklaşımı (O(n)):**
```python
def is_valid_parentheses(s):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != brackets[char]:
                return False
    
    return len(stack) == 0
```

**Çözüm Mantığı:**
1. Açılan parantezleri stack'e ekle
2. Kapatan parantez geldiğinde stack'ten çıkar
3. Eşleşme yoksa False döndür
4. Sonunda stack boş olmalı

**Time Complexity:** O(n)
**Space Complexity:** O(n)

---

### 2.6. En Büyük Alt Dizi Toplamı (Kadane Algoritması)

**Problem:** Verilen bir dizideki en büyük toplamı olan sürekli alt diziyi bul.

**Kadane Algoritması (O(n)):**
```python
def max_subarray_sum(nums):
    if not nums:
        return 0
    
    current_sum = max_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum
```

**Çözüm Mantığı:**
1. Her adımda: mevcut elemanı mı, yoksa önceki toplam + mevcut elemanı mı seç
2. Global maksimumu güncelle
3. Negatif toplam yerine 0 başla

**Time Complexity:** O(n)
**Space Complexity:** O(1)

---

### 2.7. Merge Sorted Listeler

**Problem:** İki sıralı bağlı listeyi birleştirerek yeni bir sıralı bağlı liste oluştur.

**Iterative Yaklaşım (O(n + m)):**
```python
def merge_sorted_lists(list1, list2):
    dummy = ListNode(0)
    current = dummy
    
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Kalan elemanları ekle
    current.next = list1 if list1 else list2
    
    return dummy.next
```

**Çözüm Mantığı:**
1. Dummy node ile başla
2. İki pointer ile karşılaştır
3. Küçük olanı seç ve ilerle
4. Kalan elemanları ekle

**Time Complexity:** O(n + m)
**Space Complexity:** O(1)

---

### 3.2. Ağaç Maksimum Derinliği

**Problem:** Bir ikili ağacın maksimum derinliğini bul.

**Recursive DFS (O(n)):**
```python
def max_depth_recursive(root):
    if not root:
        return 0
    
    left_depth = max_depth_recursive(root.left)
    right_depth = max_depth_recursive(root.right)
    
    return max(left_depth, right_depth) + 1
```

**Iterative BFS (O(n)):**
```python
from collections import deque

def max_depth_bfs(root):
    if not root:
        return 0
    
    queue = deque([(root, 1)])
    max_depth = 0
    
    while queue:
        node, depth = queue.popleft()
        max_depth = max(max_depth, depth)
        
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    
    return max_depth
```

**Çözüm Mantığı:**
- Recursive: Sol ve sağ alt ağaçların maksimum derinliği + 1
- BFS: Level by level traversal ile derinlik takibi

**Time Complexity:** O(n)
**Space Complexity:** O(h) (recursive), O(w) (BFS)

---

### 3.4. Ters Bağlı Liste

**Problem:** Verilen bir bağlı listeyi tersine çevir.

**Iterative Yaklaşım (O(n)):**
```python
def reverse_linked_list(head):
    prev = None
    current = head
    
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    
    return prev
```

**Recursive Yaklaşım (O(n)):**
```python
def reverse_linked_list_recursive(head):
    if not head or not head.next:
        return head
    
    new_head = reverse_linked_list_recursive(head.next)
    head.next.next = head
    head.next = None
    
    return new_head
```

**Çözüm Mantığı:**
- İki pointer kullan (prev, current)
- Her adımda pointer'ları ters çevir
- Sonunda prev yeni head olur

**Time Complexity:** O(n)
**Space Complexity:** O(1) (iterative), O(n) (recursive)

---

### 3.6. Tek Sayı Düğümü Bulma

**Problem:** Bir bağlı listede tekrar etmeyen tek bir sayıyı bul.

**Hash Table Yaklaşımı (O(n)):**
```python
def single_number_hash(head):
    seen = {}
    current = head
    
    while current:
        seen[current.val] = seen.get(current.val, 0) + 1
        current = current.next
    
    for val, count in seen.items():
        if count == 1:
            return val
    
    return None
```

**XOR Yaklaşımı (O(n)) - ÖNERİLEN:**
```python
def single_number_xor(head):
    result = 0
    current = head
    
    while current:
        result ^= current.val
        current = current.next
    
    return result
```

**Çözüm Mantığı:**
- XOR özelliği: a ^ a = 0, a ^ 0 = a
- Çift sayıda olan elemanlar birbirini yok eder
- Tek kalan eleman sonuç olur

**Time Complexity:** O(n)
**Space Complexity:** O(1) (XOR), O(n) (Hash Table)

---

### 4.2. Graf BFS/DFS

**Problem:** Bir graf üzerinde BFS ve DFS algoritmalarını uygula.

**BFS Implementation (O(V + E)):**
```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result
```

**DFS Implementation (O(V + E)):**
```python
def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    result = [start]
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))
    
    return result
```

**Çözüm Mantığı:**
- BFS: Queue kullan, level by level
- DFS: Stack/Recursion kullan, derinlik öncelikli
- Visited set ile döngü kontrolü

**Time Complexity:** O(V + E)
**Space Complexity:** O(V)

---

### 4.6. Minimum Spanning Tree (Kruskal)

**Problem:** Bir grafın minimum yayılan ağacını bul.

**Kruskal Algoritması (O(E log E)):**
```python
def kruskal_mst(edges, num_vertices):
    # Union-Find data structure
    parent = list(range(num_vertices))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        parent[find(x)] = find(y)
    
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    mst = []
    total_weight = 0
    
    for u, v, weight in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, weight))
            total_weight += weight
    
    return mst, total_weight
```

**Çözüm Mantığı:**
1. Edge'leri ağırlığa göre sırala
2. Union-Find ile cycle detection
3. Minimum weight edge'leri ekle
4. V-1 edge seçilince dur

**Time Complexity:** O(E log E)
**Space Complexity:** O(V)

---

### 5.3. Kısa Yol Algoritmaları (Dijkstra)

**Problem:** Ağırlıklı bir grafta en kısa yolu bul.

**Dijkstra Algoritması (O(V²)):**
```python
import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances
```

**Çözüm Mantığı:**
1. Priority queue kullan
2. Her adımda en kısa mesafeli vertex'i seç
3. Komşuları güncelle
4. Tüm vertex'lere ulaşınca dur

**Time Complexity:** O(V²) (array), O(E log V) (heap)
**Space Complexity:** O(V)

---

### 5.5. Network Flow (Ford-Fulkerson)

**Problem:** Bir ağda maksimum akışı bul.

**Ford-Fulkerson Algoritması (O(VE²)):**
```python
def ford_fulkerson(graph, source, sink):
    def dfs(u, flow, visited):
        if u == sink:
            return flow
        
        visited[u] = True
        
        for v, capacity in graph[u].items():
            if not visited[v] and capacity > 0:
                path_flow = dfs(v, min(flow, capacity), visited)
                if path_flow > 0:
                    graph[u][v] -= path_flow
                    graph[v][u] += path_flow
                    return path_flow
        
        return 0
    
    max_flow = 0
    
    while True:
        visited = [False] * len(graph)
        path_flow = dfs(source, float('inf'), visited)
        
        if path_flow == 0:
            break
        
        max_flow += path_flow
    
    return max_flow
```

**Çözüm Mantığı:**
1. Residual graph oluştur
2. DFS ile augmenting path bul
3. Path üzerindeki minimum capacity'yi akış olarak ekle
4. Residual graph'ı güncelle
5. Path bulunamayınca dur

**Time Complexity:** O(VE²)
**Space Complexity:** O(V²)

---

## GENEL ALGORİTMA STRATEJİLERİ

### 1. Problem Analizi
- Input/Output formatını anla
- Edge case'leri düşün
- Time/Space complexity hedefini belirle

### 2. Brute Force'dan Başla
- En basit çözümü yaz
- Time complexity'yi analiz et
- Optimizasyon fırsatlarını bul

### 3. Veri Yapısı Seçimi
- Array: Random access, O(1)
- Hash Table: Lookup, O(1)
- Stack: LIFO operations
- Queue: FIFO operations
- Tree: Hierarchical data
- Graph: Relationships

### 4. Algoritma Paradigmaları
- **Greedy**: Her adımda en iyi seçim
- **Dynamic Programming**: Subproblem çözümlerini sakla
- **Divide & Conquer**: Problemi böl ve çöz
- **Backtracking**: Tüm olasılıkları dene

### 5. Optimization Teknikleri
- **Two Pointers**: Array'de iki yönlü tarama
- **Sliding Window**: Sabit boyutlu pencere
- **Binary Search**: Sıralı veride arama
- **Prefix Sum**: Range query'ler için

---

## NOTLAR
- Bu dosya sadece referans amaçlıdır
- Önce kendi çözümünü dene
- Çözümü gördükten sonra kendi implementasyonunu yaz
- Her algoritmanın time/space complexity'sini öğren 