package main

import (
    "bytes"
    "encoding/json"
    "fmt"
    "io/ioutil"
    "log"
    "net/http"
    "os"
    "path/filepath"
    "strings"
)

type User struct {
    Name  string `json:"name"`
    Email string `json:"email"`
}

type Users []User

type Server struct {
    users Users
    port  int
}

func NewServer(port int) *Server {
    return &Server{port: port}
}

func (s *Server) Start() {
    http.HandleFunc("/", s.handleRoot)
    http.HandleFunc("/users", s.handleUsers)
    http.HandleFunc("/users/", s.handleUsers)
    http.HandleFunc("/users/new", s.handleNewUser)
    http.HandleFunc("/users/", s.handleUser)
    http.ListenAndServe(fmt.Sprintf(":%d", s.port), nil)
}

func (s *Server) handleRoot(w http.ResponseWriter, r *http.Request) {
    if r.Method == "GET" {
        fmt.Fprint(w, "<html><body><h1>Welcome to my Go web server!</h1></body></html>")
    } else {
        http.Error(w, "Method not supported", http.StatusMethodNotAllowed)
    }
}

func (s *Server) handleUsers(w http.ResponseWriter, r *http.Request) {
    if r.Method == "GET" {
        json.NewEncoder(w).Encode(s.users)
    } else {
        http.Error(w, "Method not supported", http.StatusMethodNotAllowed)
    }
}

func (s *Server) handleNewUser(w http.ResponseWriter, r *http.Request) {
    if r.Method == "POST" {
        var user User
        err := json.NewDecoder(r.Body).Decode(&user)
        if err != nil {
            http.Error(w, "Invalid request body", http.StatusBadRequest)
            return
        }
        s.users = append(s.users, user)
        w.WriteHeader(http.StatusCreated)
    } else {
        http.Error(w, "Method not supported", http.StatusMethodNotAllowed)
    }
}

func (s *Server) handleUser(w http.ResponseWriter, r *http.Request) {
    if r.Method == "GET" {
        id := filepath.Base(r.URL.Path)
        for _, user := range s.users {
            if user.Name == id {
                json.NewEncoder(w).Encode(user)
                return
            }
        }
        http.Error(w, "User not found", http.StatusNotFound)
    } else {
        http.Error(w, "Method not supported", http.StatusMethodNotAllowed)
    }
}

func main() {
    port := 8080
    server := NewServer(port)
    server.users = Users{
        {Name: "John", Email: "john@example.com"},
        {Name: "Jane", Email: "jane@example.com"},
    }
    server.Start()
    log.Printf("Server started. Listening on port %d.", port)
}
