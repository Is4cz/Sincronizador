
# Sincronizador
A principal (e única) funcionabilidade é sincronizar hora e vídeo, ou seja, se você quer que às 00:00 ele o vídeo chegue a um momento **específico** este programa foi feito para isso!!

### Como funciona
- Com a hora e o momento do vídeo em mãos ele utiliza um cálculo envolvendo múltiplicações para transformar as duas coisas "no mesmo formato" então faz a subtração e utiliza mais cálculo envolvendo divisão para transformar de volta a hora formatada no o que conhecemos *"XX:XX:XX"*.
- Então ele aguarda a hora correta, para quando chegar ele pressionar o "K" e dar play no vídeo **(Espera-se que seja utilizado no player do Youtube)**.

### Como utilizar
1. Inicie o executável do programa.
2. Adicione o momento específico do vídeo no primeiro campo, exemplo: horas:minutos:segundos.
3. Adicione o frame específico do vídeo no segundo campo, caso não tenha um coloque em 1. (Caso não saíba pode ir no Youtube e passar os frames usando `,` e `.`, então observar quando os segundos trocam).
4. Adicione o fps do vídeo no terceiro campo, para saber aperte com o botão direito do mouse e clique em "Estatítica para Nerds". Então localize a sessão "Current / Optimal Res" e então o fps, que fica após o `@`. Exemplo: Current / Optimal Res 2560x1440@**60**.
5. Adicione a hora escolhida no quarto campo, da mesma forma que no passo 2.
6. A última é uma caixinha de marcar, em que você pode decidir. Caso marcado ele irá para a outra aba aguardar o momento para dar o play, caso desmarcado ele irá apenas calcular e te entregar o momento certo para dar o play.

### Aviso
- O cálculo envolvendo frames não é tão preciso, dependendo do valor pode adiantar ou atrasar alguns frames. Porém não é motivo de tanta preucupação, já que o adiantamento ou atraso não é tão perceptível a visão humana. Acredito que isso aconteça pela divisão que ocorre durante o cálculo após a subtração.
