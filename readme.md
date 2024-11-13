# Sistema de Análise de Postura para Exercícios

Este sistema analisa a postura do usuário durante a execução de exercícios físicos, oferecendo feedback em tempo real para garantir que a posição esteja correta. Ele utiliza a biblioteca MediaPipe para detecção de pontos corporais e o OpenCV para capturar e exibir os frames de vídeo.

## Funcionalidades

- **Análise de postura**: Verifica a posição de diferentes partes do corpo e calcula ângulos entre articulações para determinar se a postura está correta.
- **Feedback em tempo real**: Exibe mensagens de feedback sobre o posicionamento dos cotovelos, quadris e joelhos para garantir uma forma correta.
- **Arquitetura extensível**: Permite a criação de diferentes exercícios usando uma fábrica (`ExerciseFactory`) que instancia o exercício desejado, possibilitando a adição de novos exercícios facilmente.

## Estrutura do Projeto

- **Core**: Contém o `ExerciseManager`, responsável por gerenciar a execução do exercício e capturar vídeo.
- **Exercises**: Define cada exercício específico. Atualmente, inclui:
  - `PlankExercise`: Exercício de prancha abdominal, verificando ângulos dos cotovelos, quadris e joelhos.
  - `IExercise`: Interface base para todos os exercícios, definindo métodos obrigatórios como `check_position` e `get_exercise_name`.
- **Factories**: Contém o `ExerciseFactory`, que cria instâncias de exercícios com base no tipo solicitado.
- **Utils**: Funções utilitárias, como `find_angle`, que calcula ângulos entre três pontos dados, usada para verificar alinhamentos corporais.
  
## Instalação

### Pré-requisitos

Certifique-se de que você tem o Python 3.x instalado e as bibliotecas necessárias (open cv e mediapipe):

```bash
pip install opencv-python mediapipe
