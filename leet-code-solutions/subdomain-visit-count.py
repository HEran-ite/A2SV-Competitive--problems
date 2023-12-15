class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visits=collections.defaultdict(int)
        res=[]
        for domain in cpdomains:
            visit,domain=domain.split()
            visit=int(visit)
            visits[domain]+=visit
            while '.' in domain:
                domain=domain.split('.',1)[1]
                visits[domain]+=visit
        for domain, visit in visits.items():
            res.append(f"{visit} {domain}")
        
        return res