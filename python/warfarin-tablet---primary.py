# S Jill Stocks, Evangelos Kontopantelis, Artur Akbarov, Sarah Rodgers, Anthony J Avery, Darren M Aschroft, 2023.

import sys, csv, re

codes = [{"code":"1781","system":"gprdproduct"},{"code":"23078","system":"gprdproduct"},{"code":"30202","system":"gprdproduct"},{"code":"30203","system":"gprdproduct"},{"code":"31511","system":"gprdproduct"},{"code":"31937","system":"gprdproduct"},{"code":"33711","system":"gprdproduct"},{"code":"34019","system":"gprdproduct"},{"code":"34086","system":"gprdproduct"},{"code":"34087","system":"gprdproduct"},{"code":"34088","system":"gprdproduct"},{"code":"34095","system":"gprdproduct"},{"code":"34299","system":"gprdproduct"},{"code":"34416","system":"gprdproduct"},{"code":"34417","system":"gprdproduct"},{"code":"34418","system":"gprdproduct"},{"code":"34517","system":"gprdproduct"},{"code":"34526","system":"gprdproduct"},{"code":"34576","system":"gprdproduct"},{"code":"34691","system":"gprdproduct"},{"code":"34758","system":"gprdproduct"},{"code":"34864","system":"gprdproduct"},{"code":"34918","system":"gprdproduct"},{"code":"39866","system":"gprdproduct"},{"code":"43407","system":"gprdproduct"},{"code":"43408","system":"gprdproduct"},{"code":"43409","system":"gprdproduct"},{"code":"45","system":"gprdproduct"},{"code":"47944","system":"gprdproduct"},{"code":"51484","system":"gprdproduct"},{"code":"51496","system":"gprdproduct"},{"code":"51509","system":"gprdproduct"},{"code":"53745","system":"gprdproduct"},{"code":"53752","system":"gprdproduct"},{"code":"54946","system":"gprdproduct"},{"code":"56314","system":"gprdproduct"},{"code":"58519","system":"gprdproduct"},{"code":"58787","system":"gprdproduct"},{"code":"58962","system":"gprdproduct"},{"code":"59578","system":"gprdproduct"},{"code":"61","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('warfarin-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["warfarin-tablet---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["warfarin-tablet---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["warfarin-tablet---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
