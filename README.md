# AdaptFL Client (Edge Device)

The **AdaptFL Client** runs on edge devices, performing local training and communicating with the server to update model weights. It listens for model updates via WebSockets and downloads new weights from Azure Blob Storage when notified.

#### AdaptFL Server (FastAPI)

🔗 [Go to AdaptFL Server Repository](https://github.com/UmarBalak/adaptfl_server)


## Features

- **Connects to FastAPI WebSocket for updates**
- **Uploads locally trained model weights to the server**
- **Downloads new global weights and updates local models**
- **Auto-reconnects on network failure**

## Setup & Installation

```bash
git clone https://github.com/UmarBalak/adaptfl_client.git
cd adaptfl_client
pip install -r requirements.txt
python data_service.py (terminal 1)
python websocket_service.py (terminal 2)
```

## Client Workflow

1. **Starts training** using the last downloaded model.
2. **Periodically uploads** locally trained weights to the server.
3. **Listens for WebSocket notifications**.
4. **Downloads new global weights** from Azure if an update is available.
5. **Updates local model** and continues training.

## Configuration

Clients must be configured with:

- `client_id`
- `api_key`
- `Azure Blob credentials`

<br>

## Overview

The **AdaptFL Server** is a FastAPI-based backend that facilitates federated learning by managing **client authentication, model aggregation, and real-time updates** via WebSockets. The server securely stores model weights in **Azure Blob Storage**, aggregates model updates from edge devices, and notifies clients when a new global model is available.

## Features

- **Client Registration & Authentication**
- **Federated Model Aggregation (FedAvg, WFA)**
- **WebSocket Notifications for Model Updates**
- **Azure Blob Storage for Model Weights**
- **API Key-Based Secure Access**
- **Auto-Reconnection for Clients**

## API Endpoints

| Method   | Endpoint                   | Description                             |
| -------- | -------------------------- | --------------------------------------- |
| **POST** | `/register`                | Register a new client                   |
| **POST** | `/upload_weights`          | Upload model weights                    |
| **GET**  | `/get_latest_model`        | Download latest global model            |
| **POST** | `/aggregate-weights`        | Aggregate weights & update global model |
| **GET**  | `/get_data`          | Get detailed system information              |
| **WS**   | `/ws/(client_id)` | WebSocket for model update alerts       |

## Workflow

1. **Client connects** to the server’s WebSocket.
2. **Clients upload local model weights** to Azure Blob Storage.
3. **Server aggregates** weights and updates the global model.
4. **Notifies clients** when a new global model is available.
5. **Clients download** the latest model and continue training.

<br>


# AdaptFL Admin Dashboard

## Overview

The **AdaptFL Admin Dashboard** is a web-based interface for monitoring active clients, model updates, and federated training progress. It provides real-time insights into the federated learning process.

## Features

- **Client Registration & Management**
- **Federated Model Monitoring**
- **Real-Time Client Connectivity Tracking**
- **Training Metrics & Performance Visualization**

## Setup & Installation

```bash
git clone https://github.com/UmarBalak/adaptfl-dash.git
cd adaptfl-dash
npm install
npm run dev
```

## Dashboard Sections

- **Active Clients:** Displays connected clients and their contributions.
- **Model Updates:** Shows federated learning aggregation progress.
- **Training Metrics and contributions:** Visualizes local model contributions and global aggregation over time.
- **Client Details:** Shows registered client details including client_id, number of contributions, current status, etc.

---
