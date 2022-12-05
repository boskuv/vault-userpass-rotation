# Vault-proxy

systemctl restart nginx.service

vault server -config ./config.hcl

export VAULT_ADDR=http://127.0.0.1:8300 // Vault must be started on a custom port
vault operator init
vault operator unseal

vault status

vault write auth/userpass/users/mitchellh     password=foo     policies=password-update-policy
vault policy list

vault auth enable userpass
vault write auth/userpass/users/test     password=foo     policies=password-update-policy

