# BTech4thYear-The-Missing-Document-Mystery

# The Missing Document Mystery

## Description
This project demonstrates a common bug in MongoDB applications: slow search performance and missing documents due to lack of indexing and incomplete data. The code simulates these issues and provides steps to fix them.

## Theme
MongoDB CRUD & Indexing

## Features
- Inserts sample documents, some with missing fields
- Simulates slow search due to missing index
- Shows how missing documents affect results
- Provides fixes: create index and patch missing documents

## How to Install
1. **Install Python 3.8+**
2. **Install dependencies:**
   ```powershell
   pip install pymongo
   ```
3. **Start MongoDB locally** (default URI: `mongodb://localhost:27017/`)

## How to Run
```powershell
python src/missing_document_mystery.py
```

## Fixing Bugs
- **Slow search:**
  - Run the script and observe search time before and after creating an index.
- **Missing documents:**
  - The script finds and patches documents missing the 'content' field.

## Customization
- Edit `src/missing_document_mystery.py` to change sample data or MongoDB URI.

## License
MIT