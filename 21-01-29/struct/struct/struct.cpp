#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

struct People
{
    string name, surname;
    int math = 0, rus = 0, phys = 0, histr = 0, sum = 0, loh = 0;
};

People make_people(string line)
{
    People a;
    string k;
    a.surname = line.substr(0, line.find(','));
    line.erase(0, line.find(',') + 1);
    a.name = line.substr(0, line.find(','));
    line.erase(0, line.find(',') + 1);
    k = line[0];
    a.math = atoi(k.c_str());
    line.erase(0, line.find(',') + 1);
    k = line[0];
    a.rus = atoi(k.c_str());
    line.erase(0, line.find(',') + 1);
    k = line[0];
    a.phys = atoi(k.c_str());
    line.erase(0, line.find(',') + 1);
    k = line[0];
    a.histr = atoi(k.c_str());
    line.erase(0, line.find(',') + 1);
    a.sum = a.histr + a.math + a.phys + a.rus;
    if (a.math == 2 or a.rus == 2 or a.phys == 2 or a.histr == 2)
    {
        a.loh = 1;
    }
    return a;
}

void print_people(People a)
{
    string s;
    s = a.surname + ' ' + a.name + ' ' + to_string(a.math) + ' ' + to_string(a.rus) + ' ' + to_string(a.phys) + ' ' + to_string(a.histr);
    cout << s << endl;
}

vector <People> sort_people(vector <People> a)
{
    People c;
    for (int i = 0; i < a.size(); i++)
    {
        for (int k = 1; k < a.size() - i; k++)
        {
            if (a[k - 1].surname > a[k].surname)
            {
                c = a[k];
                a[k] = a[k - 1];
                a[k - 1] = c;
            }
        }
    }
    return a;
}

void print_medium_score(vector <People> date)
{
    float sr = 0;
    for (int i = 0; i < date.size(); i++)
    {
        sr += date[i].math;
    }
    cout << "средний балл по алгебре " << sr / date.size() << endl;

    sr = 0;
    for (int i = 0; i < date.size(); i++)
    {
        sr += date[i].rus;
    }
    cout << "средний балл по русскому " << sr / date.size() << endl;

    sr = 0;
    for (int i = 0; i < date.size(); i++)
    {
        sr += date[i].phys;
    }
    cout << "средний балл по физике " << sr / date.size() << endl;

    sr = 0;
    for (int i = 0; i < date.size(); i++)
    {
        sr += date[i].histr;
    }
    cout << "средний балл по истории " << sr / date.size() << endl;
}
int main()
{
    setlocale(LC_ALL, "ru");
    fstream f("marks.csv");
    vector <People> date;
    int i = 0, maxsum = 0, numbers_of_loh = 0;

    if (!f)
    {
        cout << "OSHIBKA";
    }
    while (f)
    {
        string line;
        getline(f, line);
        date.push_back(make_people(line));
        maxsum = max(maxsum, date[i].sum);
        if (date[i].loh == 1) numbers_of_loh += 1;
        i += 1;
    }

    date = sort_people(date);

    print_medium_score(date);

    cout << "максимальная сумма баллов " << maxsum << endl;

    for (int i = 0; i < date.size(); i++)
    {
        if (maxsum == date[i].sum)
            cout << date[i].surname + " " + date[i].name << endl;
    }

    cout << numbers_of_loh << " человек которые получили 2" << endl;

    while (true)
    {
        int i = 0;
        cin >> i;
        if (i < 1 or i > date.size())
        {
            cout << "error";
            break;
        }
        print_people(date[i - 1]);
    }
}