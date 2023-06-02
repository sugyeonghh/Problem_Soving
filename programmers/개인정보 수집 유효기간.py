def solution(today, terms, privacies):
    d = {}
    answer = []    
    for term in terms:
        t, m = term.split(' ')
        d[t] = int(m) * 28
    
    today_days = into_days(today)
    for idx, p in enumerate(privacies):
        date, term = p.split(' ')
        p_days = into_days(date) + d.get(term)
        
        if p_days <= today_days:
            answer.append(idx + 1)
        
    return answer


def into_days(date):
    year, month, day = map(int, date.split('.'))
    return year * 12 * 28 + month * 28 + day
    