## ytDownload
ytDownload é uma ferramenta simples para baixar vídeos e músicas do YouTube diretamente pelo terminal.

### Instalação
Para instalar, basta executar o script de instalação:

```
./install.sh
```
### Como Usar
Para baixar um vídeo do YouTube, use o seguinte comando:

```
ytdownload "<url>"
```

### Parâmetros Opcionais
- `--music` ou `-m` : baixa apenas o áudio do vídeo.
- `--dir` ou `-d` : define o caminho de download desejado.

### Caminho de Download Padrão
- **Linux**: A pasta de download padrão para vídeos é Videos e para músicas é Musicas na sua home.
- **Windows**: Recomendamos que sempre utilize o parâmetro -d para especificar o caminho de download, até que seja implementado o suporte para pastas padrão no Linux.
