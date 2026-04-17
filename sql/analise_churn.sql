SELECT 
    Contract,
    COUNT(*) AS total_clientes,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churn_clientes
FROM clientes
GROUP BY Contract;
