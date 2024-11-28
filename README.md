# ytDownload
ytDownload é uma ferramenta simples para baixar vídeos e músicas do YouTube diretamente pelo terminal.

## depedências
- FFmpeg

## Instalar FFmpeg no Windows
Acesse a página oficial: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html).
Baixe a versão estática para Windows.
Extraia os Arquivos:

Extraia o conteúdo do arquivo .zip em um local permanente, como C:\ffmpeg.
Adicione ao PATH:

Abra o menu Iniciar e procure por "Editar as variáveis de ambiente do sistema".

Clique em "Variáveis de Ambiente".

Na seção "Variáveis do Sistema", selecione Path e clique em "Editar".

Clique em "Novo" e adicione o caminho para a pasta bin do FFmpeg, como:
makefile
Copiar código
C:\ffmpeg\bin

Clique em "OK" para salvar.


## FFmpeg no linux

```
sudo apt install ffmpeg -y
```

## Instalação
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
- **Windows**: Recomendamos que sempre utilize o parâmetro `-d` para especificar o caminho de download, até que seja implementado o suporte para pastas padrão no Windows.
