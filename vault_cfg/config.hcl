storage "file" {
  path = "./vault-data"
}
listener "tcp" {
  address = "127.0.0.1:8300"
  tls_disable = "true"
}

disable_mlock = true

api_addr = "http://127.0.0.1:8300"
cluster_addr = "https://127.0.0.1:8301"
ui = true


