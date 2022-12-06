# Vault-userpass-rotation

Configure nginx (https://mohsensy.github.io/sysadmin/2018/02/08/nginx-reverse-proxy.html)
systemctl restart nginx.service

vault server -config ./config.hcl

export VAULT_ADDR=http://127.0.0.1:8300 // Vault must be started on a custom port
vault operator init
vault operator unseal

vault status

vault login (use root token)

vault policy write password-update-policy ./password-update-policy.hcl
vault policy list

vault auth enable userpass
vault write auth/userpass/users/test     password=foo     policies=password-update-policy

