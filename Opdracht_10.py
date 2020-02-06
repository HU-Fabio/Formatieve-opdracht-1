def fibonaci(n):
    if n <= 1:
        return n
    else:
        # Omdat de waarde van term N te berekenen
        # Tel je de 2 voorgaande waardes van de termen bij elkaar op
        return fibonaci(n - 1) + fibonaci(n - 2)


