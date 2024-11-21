Commande ECHO activ�e.

---

### 3. **UPDATE** (`update.md`)
**Contenu du fichier `update.md`** :
```markdown
# UPDATE Operation

## Commande utilisée
```python
# Récupérer un objet existant
book = Book.objects.get(id=1)

# Mettre à jour le titre du livre
book.title = "Advanced Django"
book.save()
