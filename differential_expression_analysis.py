library("DESeq2")

# Load the count matrix
count_data <- read.csv("/path/to/counts.csv", row.names = 1)
col_data <- read.csv("/path/to/coldata.csv", row.names = 1)

# Create DESeq2 dataset
dds <- DESeqDataSetFromMatrix(countData = count_data, colData = col_data, design = ~ condition)

# Run DESeq2 analysis
dds <- DESeq(dds)

# Get results
res <- results(dds)

# Save results to a file
write.csv(as.data.frame(res), file = "/path/to/differential_expression_results.csv")
