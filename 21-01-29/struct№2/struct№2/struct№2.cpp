#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <cstring>
#include <algorithm>

using namespace std;

struct files
{
    string name = "", type = "", date_of_create = "", date_of_change = "", access = "";
    int mass = 0;
};

files str_in_struct(string s)
{
    files a;

    a.name = s.substr(0, s.find(","));
    s.erase(0, s.find(",") + 1);

    a.mass = atoi(s.substr(0, s.find(",")).c_str());
    s.erase(0, s.find(",") + 1);

    a.type = s.substr(0, s.find(","));
    s.erase(0, s.find(",") + 1);

    a.date_of_create = s.substr(0, s.find(","));
    s.erase(0, s.find(",") + 1);

    a.date_of_change = s.substr(0, s.find(","));
    s.erase(0, s.find(",") + 1);

    a.access = s.substr(0, s.size());
    s.erase(0, s.find(",") + 1);

    return a;
}

void print_file(files a)
{
    string s;
    s = a.name + ' ' + to_string(a.mass) + ' ' + a.type + ' ' + a.date_of_create + ' ' + a.date_of_change + ' ' + a.access;
    cout << s << endl;
}
bool sravn_name(files left, files right)
{
    return left.name < right.name;
}

void sort_files_by_name(vector <files> &a)
{
    sort(a.begin(), a.end(), sravn_name);
}

bool sravn_size(files left, files right)
{
    return left.mass > right.mass;
}

void sort_files_by_size(vector <files>& a)
{
    sort(a.begin(), a.end(), sravn_size);
}

int main()
{
    setlocale(LC_ALL, "ru");
    fstream f("files.csv");
    vector <files> date;
    string s;
    vector <string> type;
    vector <int> number_of_type;
    int i = 0;
    int n;
    
    while (f)
    {
        getline(f, s);
        date.push_back(str_in_struct(s));
        n = -1;
        for (int k = 0; k < type.size(); k++)
        {
            if (type[k] == date[i].type)
            {
                n = k;
                break;
            }
        }
        if (n == -1)
        {
            type.push_back(date[i].type);
            number_of_type.push_back(0);
            n = type.size() - 1;
        }
        number_of_type[n] += 1;
        i += 1;
    }
    date.pop_back();
    number_of_type[n] -= 1;
    
    for (int i = 0; i < type.size(); i++)
    {
        cout << type[i] << " " << number_of_type[i] << endl;
    }
    cout << endl;

    sort_files_by_size(date);
    vector <files> biges;
    for (int i = 0; i < 10; i++)
    {
        biges.push_back(date[i]);
    }
    sort_files_by_name(biges);
    for (int i = 0; i < 10; i++)
    {
        cout << biges[i].name << " " << biges[i].mass << endl;
    }
    cout << endl;

    vector <files> pdf;
    for (int i = 0; i < date.size(); i++)
    {
        files a = date[i];
        //print_file(date[i]);
        if (a.access == "ограничен" and a.date_of_change.find("2012") != string::npos and a.type == "презентация")
            pdf.push_back(a);
    }
    sort_files_by_name(pdf);
    for (int i = 0; i < pdf.size(); i++)
        print_file(pdf[i]);
    cout << endl;

    vector <files> video;
    for (int i = 0; i < date.size(); i++)
    {
        files a = date[i];
        //print_file(date[i]);
        if (a.date_of_create[3] + a.date_of_create[4] > 6 and a.date_of_create.find("2011") != string::npos and a.type == "видео" and a.mass > 102400)
            video.push_back(a);
    }
    sort_files_by_size(video);
    for (int i = video.size() - 1; i >= 0; i--)
        print_file(video[i]);
    return 0;
}
