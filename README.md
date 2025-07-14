# Financial Hedging System

This project is a Python-based backend system that helps financial analysts or portfolio managers automate the pricing, evaluation, and rebalancing of hedging strategies for portfolios exposed to market, interest rate, foreign exchange, or commodity risks.

## Key Features

*   **Derivative Pricing Engine**: Use QuantLib to price options, forwards, and swaps.
*   **Risk Sensitivity Analysis**: Calculate and expose Greeks: Delta, Gamma, Vega, Theta, Rho.
*   **Hedge Effectiveness Evaluation**: Compare current portfolio exposure vs. hedged position.
*   **API Interface (FastAPI)**: Expose the functionality of the system through a REST API.
*   **Portfolio Input**: Accept user portfolios via API or load from Supabase.
*   **Scheduling and Rebalancing**: Use Celery for scheduled revaluation of derivatives and hedge positions.
*   **Secure Authentication (JWT)**: Secure the API with JWT authentication.

## Getting Started

1.  **Install dependencies**:
    ```bash
    poetry install
    ```
2.  **Run the application**:
    ```bash
    poetry run uvicorn src.main:app --reload
    ```

## API Endpoints

*   `POST /hedge/price-option`: Price a derivative.
*   `GET /`: Hello World

## Running Tests

```bash
poetry run pytest
```
