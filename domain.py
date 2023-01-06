class Solution:
  def subdomainVisits(self,cpdomain):
    count= { }
    for domain in cpdomain:
      visits= int(domain.split()[0])
      domain_segments= domain.split()[0].split('.')
      top_level_domain= domain_segments[-1]
      sec_level_domain= domain_segments[-2]+'.'+domain_segments[-1]
      count[top_level_domain]= count[top_level_domain]+visits if top_level_domain in count_keys() else visits
      count[sec_level_domain]= count[sec_level_domain]+visits if sec_level_domain in count_keys() else visits
      if domain.count('.')== 2:
        count[domain.split()[1]]=  count[domain.split()[1]]+visits if domain.split()[1] in count.keys()else visits
    return [str(v)+''+k for k,v in count.items()]
if __name__== "__main__":
  solution= Solution()
  inputnum= ['1201 school.bupt.edu']
  print("输入:",inputnum)
  print("输入:",solution.subdomainVisits(inputnum))
