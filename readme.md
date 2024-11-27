# Sistema de Análise de Postura para Exercícios

Este sistema realiza análise de postura em tempo real para diferentes exercícios físicos, garantindo que os movimentos sejam executados corretamente. Ele utiliza a biblioteca MediaPipe para rastreamento corporal e OpenCV para captura e exibição de vídeo.

## Funcionalidades

- **Análise de postura automatizada**:
  - Verifica ângulos corporais entre articulações em tempo real.
  - Identifica desvios de postura e orienta ajustes.
- **Feedback em tempo real**:
  - Mensagens visuais e métricas sobre desempenho.
  - Destaque de erros como desalinhamento dos cotovelos, quadris e joelhos.
- **Arquitetura modular e extensível**:
  - Exercícios definidos como classes especializadas.
  - Fácil integração de novos exercícios via `ExerciseFactory`.
- **Métricas detalhadas ao final**:
  - Total de repetições realizadas.
  - Tempo total e eficiência por repetição.
  - Calorias estimadas durante o exercício.

## Estrutura do Projeto

### Diretórios Principais

1. **Core**:
   - Contém o `ExerciseManager`, gerenciando:
     - Fluxo de entrada de vídeo (câmera ou arquivos).
     - Modos de execução (tempo, repetições ou padrão).
     - Interação com exercícios específicos.
2. **Exercises**:
   - Classes para diferentes exercícios com validação de posturas:
     - **`PlankExercise`**: Verifica alinhamento em pranchas abdominais.
     - **`PushUpExercise`**: Monitora flexões de braço, focando em ângulos dos cotovelos e alinhamento corporal.
     - **`AbdominalRowerExercise`**: Analisa ângulos para exercícios abdominais remadores.
   - Todas implementam a interface base `Exercise`.
3. **Factories**:
   - `ExerciseFactory`:
     - Criação dinâmica de exercícios com base no tipo informado.
4. **Utils**:
   - Função `find_angle`: Cálculo preciso de ângulos entre três pontos, base para validação de posturas.

## Detalhes de Implementação

### Classes Principais

#### `ExerciseManager`

Gerencia a captura de vídeo, análise de postura e controle do fluxo principal do programa.

- **Métodos Chave**:
  - `run()`: Captura frames e delega a validação de posturas à classe de exercício ativa.
  - `display_final_metrics()`: Exibe estatísticas detalhadas no término do exercício.

#### `Exercise`

Interface abstrata base para todos os exercícios.

- **Métodos Obrigatórios**:
  - `check_position()`: Valida a postura com base nos landmarks detectados.
  - `get_exercise_name()`: Retorna o nome do exercício.
  - `find_angle()`: Calcula ângulos entre três pontos.

#### `ExerciseFactory`

Fábrica responsável por instanciar exercícios com base em strings identificadoras.

- Exercícios suportados:
  - `"plank"`: Prancha abdominal.
  - `"push-up"`: Flexões de braço.
  - `"abdominal_rower"`: Abdominais remadores.

### Modos de Execução

- **Tempo**: Avaliação de posturas durante um intervalo definido.
- **Repetições**: Contagem de movimentos corretos até atingir uma meta.
- **Padrão**: Análise baseada em um vídeo sem contagem ou limites.

## Instalação

### Pré-requisitos

- Python 3.8 ou superior.
- Bibliotecas necessárias:
  ```bash
  pip install opencv-python mediapipe numpy
