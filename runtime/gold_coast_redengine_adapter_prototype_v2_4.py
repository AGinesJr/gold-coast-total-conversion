"""Gold Coast runtime adapter prototype; EngineBridge is a test double, not REDengine."""
class EngineBridge:
    def __init__(self): self.facts={}; self.objectives={}; self.quests={}; self.events=[]
    def set_fact(self,k,v): self.facts[k]=v
    def add_fact(self,k,v): self.facts[k]=self.facts.get(k,0)+v
    def objective(self,k,v): self.objectives[k]=v
    def emit(self,e,p): self.events.append((e,p))
class GoldCoastAdapter:
    ALLOWED={"SET_FLAG","ADD","START_OBJECTIVE","COMPLETE_OBJECTIVE","RESET_OBJECTIVE","RESTORE_CHECKPOINT","RESET_QUEST","COMPLETE_QUEST"}
    def __init__(self,bridge=None): self.bridge=bridge or EngineBridge()
    def commands(self,items):
        for c in items:
            op=c["op"]
            if op not in self.ALLOWED: raise ValueError("Blocked command "+op)
            if op=="SET_FLAG": self.bridge.set_fact(c["path"],c["value"])
            elif op=="ADD": self.bridge.add_fact(c["path"],c["value"])
            elif op=="START_OBJECTIVE": self.bridge.objective(c["id"],"ACTIVE")
            elif op=="COMPLETE_OBJECTIVE": self.bridge.objective(c["id"],"COMPLETE")
            elif op=="RESET_OBJECTIVE": self.bridge.objective(c["id"],"RESET")
            else: self.bridge.emit(op,c)
    def dispatch(self,pool,district,event):
        if pool["district"]!=district or pool["eventType"]!=event:return None
        return sorted(pool["records"],key=lambda r:r["priority"])[0] if pool["records"] else None
    def integration_contract(self):
        return {"dialogue":"bind speaker/text/locKey to verified dialogue resources","choices":"map CHOICE edges to choice records","questFacts":"map context flags to quest facts","triggers":"bind event pools to world/quest callbacks","commands":"map allowlisted commands to verified script APIs","test":"in-game smoke tests required"}
