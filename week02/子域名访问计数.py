# linkfor:https://leetcode-cn.com/problems/subdomain-visit-count/
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        map = {}
        for item in cpdomains:
            arr = str(item).split(' ')
            count = int(arr[0])
            domainname = str(arr[1])
            while domainname.__contains__('.'):
                map[domainname] = map.get(domainname, 0) + count
                domainname = domainname[domainname.index('.')+1:]
            map[domainname] = map.get(domainname, 0) + count
        result = []
        for key in map:
            string = str(map.get(key)) + " " + key
            result.append(string)
        return result
