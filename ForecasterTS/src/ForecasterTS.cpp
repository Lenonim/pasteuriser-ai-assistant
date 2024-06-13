#include "ForecasterTS.h"

using namespace std;

int main()
{
    clock_t start, finish;
    double  duration;
    long long i_time = 0;

    vector<OCDF> data;

	std::ifstream load_file;
	OneCIDDataFormat f_temp_data;
    OneCIDDataFormat s_temp_data;
    char buffer_char;
	load_file.open("data_example.csv");

    int input_range;
    int output_range;

    OCDFNeuron* mmodel = new TInOCDFVanilaLSTM();;
    mmodel->load_model("model_example.tlstm");
    AbstractActivator* main_activator = new Logistic();
    AbstractActivator* additional_activator = new Tanh();
    mmodel->set_main_activator(main_activator);
    mmodel->set_additional_activator(additional_activator);
    input_range = mmodel->get_input_range();
    output_range = mmodel->get_output_range();
    delete mmodel;

    start = clock();
    while (true) {
        finish = clock();
        duration = (double)(finish - start) / CLOCKS_PER_SEC;
        if (duration >= double(i_time + 1)) {
            std::cout << "time = " << duration << "\n\n";

            load_file >> f_temp_data.cid >> buffer_char >> f_temp_data.time >> buffer_char >> f_temp_data.value;
            load_file >> s_temp_data.cid >> buffer_char >> s_temp_data.time >> buffer_char >> s_temp_data.value;
            
            if (data.size() == 2 * input_range) {
                string arguments = std::to_string(data[0].time) + " " + std::to_string(data[2].time - data[0].time);
                for (size_t i = 2; i < 2 * input_range; i++) {
                    data[i - 2] = data[i];
                    arguments += " " + std::to_string(data[i].value);
                }

                data[data.size() - 2] = f_temp_data;
                data[data.size() - 1] = s_temp_data;

                cout << "target:\t\t";
                for (size_t i = 0; i < 2 * input_range; i = i + 2) {
                    printf("%2.4f", data[i].value);
                    cout << "\t";
                }
                cout << "\n";

                cout << "other:\t\t";
                for (size_t i = 1; i < 2 * input_range; i = i + 2) {
                    printf("%2.4f", data[i].value);
                    cout << "\t";
                }
                cout << "\n";

                arguments = "ForecasterTS.exe " + arguments + " " + std::to_string(f_temp_data.value) + " " + std::to_string(s_temp_data.value);

                OCDFNeuron* model = new TInOCDFVanilaLSTM();;
                model->load_model("model_example.tlstm");
                AbstractActivator* main_activator = new Logistic();
                AbstractActivator* additional_activator = new Tanh();
                model->set_main_activator(main_activator);
                model->set_additional_activator(additional_activator);

                std::vector<OCDF> predicts = model->predict(data);

                std::cout << "predicts:\t";
                for (size_t i = 0; i < predicts.size(); i++) {
                    printf("%2.4f", predicts[i].value);
                    std::cout << "\t";
                }
                std::cout << "\n";

                model->save_model("model_example.tlstm");
                delete model;

                //system(arguments.c_str());
            }
            else {
                data.push_back(f_temp_data);
                data.push_back(s_temp_data);
            }

            cout << "\n";

            i_time++;
        }
    }

    load_file.close();
}
