Commande ECHO activ�e.

---

### 2. **RETRIEVE** (`retrieve.md`)
**Contenu du fichier `retrieve.md`** :
```markdown
# RETRIEVE Operation

## Commande utilisée
### Récupérer tous les livres
```python
books = Book.objects.all()
for book in books:
    print(book)
