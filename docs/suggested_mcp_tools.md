# Suggested MCP Trading & Finance Tools for Binance MCP Server

This document lists tools (features/modules/endpoints) for the Binance Model Context Protocol (MCP) server, each with a detailed name, description, and alternative nomenclature. All tools are strictly focused on trading and finance.

## 1. get_balance
- **Purpose:** Retrieve user’s account balances (spot, margin, futures).
- **Alternatives:** fetch_account_balance, account_balance_info

## 2. get_portfolio
- **Purpose:** Fetch current holdings, open positions, and asset allocation.
- **Alternatives:** fetch_portfolio, portfolio_info

## 3. get_market_data
- **Purpose:** Provide real-time and historical price, volume, and order book data.
- **Alternatives:** fetch_market_data, market_data_feed

## 4. place_order
- **Purpose:** Submit new buy/sell orders (market, limit, stop, etc.).
- **Alternatives:** create_order, submit_order

## 5. cancel_order
- **Purpose:** Cancel open orders by ID or symbol.
- **Alternatives:** remove_order, revoke_order

## 6. get_order_status
- **Purpose:** Retrieve status and details of specific orders.
- **Alternatives:** fetch_order_status, order_info

## 7. list_orders
- **Purpose:** List all open, filled, or cancelled orders for a user.
- **Alternatives:** get_orders, fetch_order_list

## 8. get_trade_history
- **Purpose:** Fetch historical trades executed by the user.
- **Alternatives:** fetch_trade_history, trade_log

## 9. get_funding_rates
- **Purpose:** Retrieve funding rates for futures/perpetual contracts.
- **Alternatives:** fetch_funding_rates, funding_info

## 10. get_transaction_history
- **Purpose:** List deposits, withdrawals, and transfers.
- **Alternatives:** fetch_transaction_history, transaction_log

## 11. get_pnl
- **Purpose:** Calculate and return realized/unrealized profit and loss.
- **Alternatives:** fetch_pnl, profit_and_loss

## 12. get_risk_metrics
- **Purpose:** Provide margin level, liquidation risk, and leverage info.
- **Alternatives:** fetch_risk_metrics, risk_info

## 13. get_fee_info
- **Purpose:** Retrieve trading, withdrawal, and funding fee rates.
- **Alternatives:** fetch_fee_info, fee_rates

## 14. get_ticker
- **Purpose:** Fetch latest price and 24h stats for a symbol.
- **Alternatives:** fetch_ticker, ticker_info

## 15. get_order_book
- **Purpose:** Retrieve current order book (bids/asks) for a symbol.
- **Alternatives:** fetch_order_book, orderbook_info

## 16. get_position_info
- **Purpose:** Get details on open positions (size, entry, liquidation).
- **Alternatives:** fetch_position_info, position_details

## 17. get_leverage_brackets
- **Purpose:** Fetch allowed leverage and margin requirements.
- **Alternatives:** fetch_leverage_brackets, leverage_info

## 18. get_asset_price
- **Purpose:** Retrieve current or historical price for a specific asset.
- **Alternatives:** fetch_asset_price, asset_price_info

## 19. get_account_snapshot
- **Purpose:** Get a point-in-time snapshot of account state.
- **Alternatives:** fetch_account_snapshot, account_state

## 20. get_margin_interest
- **Purpose:** Retrieve interest rates and accrued interest for margin trading.
- **Alternatives:** fetch_margin_interest, margin_interest_info

## 21. get_liquidation_history
- **Purpose:** List past liquidation events for the account.
- **Alternatives:** fetch_liquidation_history, liquidation_log

## 22. get_dividends
- **Purpose:** Retrieve dividend payments and history for assets.
- **Alternatives:** fetch_dividends, dividend_history

## 23. get_borrow_history
- **Purpose:** Fetch history of borrowed funds and repayments (margin/futures).
- **Alternatives:** fetch_borrow_history, borrow_log

## 24. get_asset_transfer
- **Purpose:** Retrieve and initiate asset transfers between accounts (spot, margin, futures).
- **Alternatives:** fetch_asset_transfer, transfer_funds

## 25. get_withdrawal_status
- **Purpose:** Check status of withdrawal requests.
- **Alternatives:** fetch_withdrawal_status, withdrawal_info

## 26. get_available_assets
- **Purpose:** Retrieve the list of available assets and their names.
- **Alternatives:** fetch_available_assets, asset_list, list_assets
---

These tool names and alternatives are designed for clarity, maintainability, and direct relevance to trading and finance for developers integrating with the Binance MCP server.
