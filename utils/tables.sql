-- Table: stocks
CREATE TABLE stocks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol TEXT NOT NULL UNIQUE,
    name TEXT,
    market TEXT -- e.g., NASDAQ, NYSE
);

-- Table: stock_prices
CREATE TABLE stock_prices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    stock_id INTEGER,
    date TEXT, -- ISO format: YYYY-MM-DD
    price REAL,
    FOREIGN KEY (stock_id) REFERENCES stocks(id)
);

-- Table: stock_metrics (for dashboard view)
CREATE TABLE stock_metrics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    stock_id INTEGER,
    current_price REAL,
    week52_low REAL,
    week52_high REAL,
    percent_from_52low REAL,
    percent_from_52high REAL,
    percent_change_30d REAL,
    percent_change_90d REAL,
    created_at TEXT, -- timestamp
    FOREIGN KEY (stock_id) REFERENCES stocks(id)
);

-- Table: revenue_projections
CREATE TABLE revenue_projections (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    stock_id INTEGER,
    year INTEGER,
    revenue_estimate REAL,
    FOREIGN KEY (stock_id) REFERENCES stocks(id)
);

-- Table: uploaded_documents (for OpenAI File Search)
CREATE TABLE uploaded_documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    stock_id INTEGER,
    file_name TEXT,
    openai_file_id TEXT, -- ID from OpenAI File API
    uploaded_at TEXT,
    FOREIGN KEY (stock_id) REFERENCES stocks(id)
);

-- Optional Table: top_companies_by_metric (from web search)
CREATE TABLE top_companies_by_metric (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    metric TEXT, -- e.g., 'revenue', 'EPS'
    rank INTEGER, -- 1 to N
    stock_symbol TEXT,
    company_name TEXT,
    value REAL,
    source_url TEXT,
    fetched_at TEXT -- timestamp
);
