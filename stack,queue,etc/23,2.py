def hacer_album(artista, titulo, canciones=None):
    album = {"artista": artista, "titulo": titulo}
    if canciones:
        album["canciones"] = canciones
    return album

print(hacer_album("A", "B"))
print(hacer_album("C", "D", 10))