import requests

class Mulu:
    def __init__(self):
        pass

    def get_mulu_txt(self, filename):
        with open(f"{filename}", "r") as file:
            # 去除\n换行方法
            mulu_list = file.read().splitlines()
        return mulu_list

    def get_url_pinjie_ceshi(self, url, mulu_list):
        new_url_list = []
        for mulu in mulu_list:
            new_url = url+'/'+mulu
            res = requests.get(new_url)
            if res.status_code == 200 or res.status_code == 302 or res.status_code == 403:
                new_url_list.append(new_url)
        return new_url_list

    def cun_ok_url(self, filename, new_url_list):
        with open(f"{filename}.txt", "w+", newline="") as f:
            for value in new_url_list:
                f.write(value+'\n')


if __name__ == '__main__':
    mulu = Mulu()
    url = input("请输入要扫描的url：")
    filename = input("请输入要存入的文件名：")
    mulu_list = mulu.get_mulu_txt('mulu.txt')
    print(mulu.get_url_pinjie_ceshi(url, mulu_list))
    mulu.cun_ok_url(filename, mulu.get_url_pinjie_ceshi(url, mulu_list))
