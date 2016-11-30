#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_map>
using namespace std;

class Node {
    public:
    	unordered_map<char, Node*> map;
   		bool end;
   		Node();
};

Node::Node() {
	end = false;
}

class Trie {
    Node* root;
    public: 
        bool add(string s);
        Trie();
};

Trie::Trie() {
	root = new Node();
}

bool Trie::add(string s) {
    Node* aux = root;
    for(int i = 0; i < s.length(); i++) {
        auto it = aux->map.find(s[i]);
        if(it != aux->map.end()) {
            aux = it->second;
            if(aux->end) {
                return false;
            }
        }
        else {
            Node* nuevo = new Node;
            aux->map.insert({s[i], nuevo}); 
            aux = nuevo;
        }
    }
    if(aux->map.empty()) {
        aux->end = true;
        return true;
    }
    return false;
}


int main() {
    int n;
    Trie trie;
    string helper;
    cin >> n;
    for(int i = 0; i < n; ++i) {
        cin >> helper;
        if(!trie.add(helper)) {
            cout << "BAD SET" << endl;
            cout << helper << endl;
            return 0;
        }
    }
    cout << "GOOD SET" << endl;
    return 0;
}
