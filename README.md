# Automação de Captura Manual

Este script Python foi desenvolvido para automatizar o processo de inserção de informações de transações de pagamento em um sistema específico. Ele utiliza a biblioteca PyAutoGUI para simular interações com o teclado e o mouse.

## Pré-requisitos

Certifique-se de ter instalado o Python e a biblioteca PyAutoGUI. Você pode instalá-la via pip:

```bash
pip install pyautogui
```


## Uso

1. Execute o script em um ambiente Python compatível.
2. Certifique-se de que o arquivo de entrada `automacaocapturamanual.txt` esteja presente no mesmo diretório do script. Este arquivo deve conter as informações das transações a serem inseridas no sistema, separadas por ponto e vírgula (`;`), sendo a ordem: paymentId, img, tid, status e valor.
3. Abra o sistema onde deseja inserir as informações manualmente.
4. Aguarde a execução do script.

## Funcionamento

1. O script aguardará por 3 segundos e então alternará para a janela do sistema alvo.
2. Para cada linha no arquivo de entrada, o script realizará as seguintes ações:
   - Extrair as informações de `paymentId`, `tid`, `status` e `valor`.
   - Colar o `paymentId` em um campo específico no sistema.
   - Colar o `tid` em outro campo específico no sistema.
   - Definir o `status` como "Approved".
   - Inserir o `valor` da transação.
3. Após cada ação, o script aguardará um intervalo de tempo para garantir que as operações sejam concluídas corretamente.

## Observações

- Certifique-se de ajustar as coordenadas dos cliques (`pyautogui.click()`) de acordo com a interface do sistema em que está trabalhando.
- O script assume que as coordenadas e os elementos da interface do sistema permanecem constantes entre as execuções.

## Avisos de Responsabilidade

- Este script foi desenvolvido para fins educacionais e de demonstração.
- Use-o com cuidado, pois interage diretamente com a interface do usuário e pode causar efeitos indesejados se usado incorretamente.
