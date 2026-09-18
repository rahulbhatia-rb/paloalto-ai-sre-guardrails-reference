from dataclasses import dataclass
@dataclass(frozen=True)
class Signal: confidence:float; error_budget:float; blast_radius:int; approved:bool
def action(s:Signal)->str:
 if s.error_budget<.2:return 'escalate-protect-reliability'
 if not s.approved or s.confidence<.9 or s.blast_radius>1:return 'propose-for-review'
 return 'execute-bounded-remediation'
