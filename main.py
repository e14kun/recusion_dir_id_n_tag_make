# docu_srch_jy_test.clsn_m 부모자식 폴더트리 query 카테고리 생성기
# 2024/06/21 by ljy

import os

def d_tree(directory="",directory_id=0,lvl=0,all_path="",parent_id=0,d_tag=[],sort_num=0):
    if all_path != "":
        all_path = f"{all_path}/{directory}"

    if lvl != 0:
        old_d_tag = d_tag[:]
        d_tag.append(f"{directory}({directory_id})")
        sort_num=sort_num+1
        print(f"(sort:{sort_num:02d} / lvl:{lvl}) {lvl*' -- '}{directory}(id:{directory_id} / pa:{parent_id}) : {d_tag}")

    d_list = os.listdir(all_path)
    if len(d_list)==0:
        return directory_id,parent_id,old_d_tag,sort_num
    else:
        new_parent_id=directory_id
        old_d_tag=d_tag[:]
        for now_d in d_list:
            # print(f"{all_path}/{now_d}")
            if os.path.isfile(f"{all_path}/{now_d}"):
                continue
            directory_id,parent_id,old_d_tag,sort_num = d_tree(now_d,directory_id=directory_id+1,lvl=lvl+1,all_path=all_path,parent_id=new_parent_id,d_tag=old_d_tag,sort_num=sort_num)
        if len(old_d_tag)>0:
            del old_d_tag[-1]
        return directory_id,parent_id,old_d_tag,sort_num


# Example usage
if __name__ == "__main__":
    target_directory = "target_folder"
    print("---- start -----")
    d_tree(all_path=target_directory)
    print("---- end -----")
