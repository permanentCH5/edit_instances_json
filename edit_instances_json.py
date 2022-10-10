from __future__ import annotations
import json
import glob
# import ijson
def main():
    # 比如做人（person，只有一类，id1）
    # 以及车辆（vehicle，id2-9分别是bicycle,car,motorcycle,airplane,bus,train,truck,boat）
    # 以及动物的分类（id16-25，分别是bird,cat,dog,horse,sheep,cow,elephant,bear,zebra,giraffe）。
    # file_name = '.\\data\\coco\\annotations\\instances_train2017.json'
    # written_json_name = ".\\data\\coco\\annotations\\train_person.json"
    file_name = '.\\data\\coco\\annotations\\instances_val2017.json'
    written_json_name = ".\\data\\coco\\annotations\\val_person.json"

    # file_name = '.\\data\\coco\\annotations\\instances_train2017.json'
    # written_json_name = ".\\data\\coco\\annotations\\train_vehicle.json"
    # file_name = '.\\data\\coco\\annotations\\instances_val2017.json'
    # written_json_name = ".\\data\\coco\\annotations\\val_vehicle.json"

    # file_name = '.\\data\\coco\\annotations\\instances_train2017.json'
    # written_json_name = ".\\data\\coco\\annotations\\train_animal.json"
    # file_name = '.\\data\\coco\\annotations\\instances_val2017.json'
    # written_json_name = ".\\data\\coco\\annotations\\val_animal.json"


    write_dict = {}
    
    annos = json.loads(open(file_name).read())
    write_dict['info'] = annos['info']
    write_dict['licenses'] = annos['licenses']
    write_dict['images'] = []
    write_dict['annotations'] = []
    write_dict['categories'] = [{"supercategory": "person","id": 1,"name": "person"}]
    
    # write_dict['categories'] = [{"supercategory": "vehicle","id": 2,"name": "bicycle"},
    #                             {"supercategory": "vehicle","id": 3,"name": "car"},
    #                             {"supercategory": "vehicle","id": 4,"name": "motorcycle"},
    #                             {"supercategory": "vehicle","id": 5,"name": "airplane"},
    #                             {"supercategory": "vehicle","id": 6,"name": "bus"},
    #                             {"supercategory": "vehicle","id": 7,"name": "train"},
    #                             {"supercategory": "vehicle","id": 8,"name": "truck"},
    #                             {"supercategory": "vehicle","id": 9,"name": "boat"}]
    
    # write_dict['categories'] = [{"supercategory": "animal","id": 16,"name": "bird"},
    #                             {"supercategory": "animal","id": 17,"name": "cat"},
    #                             {"supercategory": "animal","id": 18,"name": "dog"},
    #                             {"supercategory": "animal","id": 19,"name": "horse"},
    #                             {"supercategory": "animal","id": 20,"name": "sheep"},
    #                             {"supercategory": "animal","id": 21,"name": "cow"},
    #                             {"supercategory": "animal","id": 22,"name": "elephant"},
    #                             {"supercategory": "animal","id": 23,"name": "bear"},
    #                             {"supercategory": "animal","id": 24,"name": "zebra"},
    #                             {"supercategory": "animal","id": 25,"name": "giraffe"}]
    
    category_list = [1]
    # category_list = [i for i in range(2,10)]
    # category_list = [i for i in range(16,26)]
    
    
    image_use_list = []
    print(len(annos['annotations']))
    
    for i in range(0,len(annos['annotations'])):
        anno_dict = {}
        if annos['annotations'][i]['category_id'] in category_list:
            image_id = annos['annotations'][i]['image_id']
            if image_id not in image_use_list:
                image_use_list.append(image_id)
            anno_dict['image_id'] = annos['annotations'][i]['image_id']
            anno_dict['bbox'] = annos['annotations'][i]['bbox']
            anno_dict['category_id'] = annos['annotations'][i]['category_id']
            anno_dict['id'] = annos['annotations'][i]['id']
            anno_dict['area'] = annos['annotations'][i]['area']
            anno_dict['iscrowd'] = annos['annotations'][i]['iscrowd']
            write_dict['annotations'].append(anno_dict)
        if i % 1000 == 0:
            print(i)
                
        
        
    for i in range(0,len(annos['images'])):
        if annos['images'][i]["id"] in image_use_list:
            write_dict['images'].append(annos['images'][i])
            
    
    json_str = json.dumps(write_dict)
    with open(written_json_name,"w") as f:
        f.write(json_str)

if __name__=='__main__':
    main()