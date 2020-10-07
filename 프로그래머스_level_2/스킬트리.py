def solution(skill, skill_trees):
    answer = 0
    d = [False] * 26
    
    for sk in skill_trees:
        for i in range(1, len(skill)):
            index = ord(skill[i]) - ord('A')
            d[index] = True

        skill_index = 0
        flag = False

        for i in range(len(sk)):
            if d[ord(sk[i]) - ord('A')]:
                
                flag = True
                break
            if skill[skill_index] == sk[i]:
                skill_index+=1
                if skill_index >= len(skill): 
                    skill_index-=1
                    continue
                d[ord(skill[skill_index]) - ord('A')] = False
        if not flag:
            answer+=1
    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))