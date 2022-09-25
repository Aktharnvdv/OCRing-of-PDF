import re


def Find_Keys_and_Values(i,RESP_DICT):

    print(i)
    j = 0

    RESP_DICT["data"]["code"] = 200
    RESP_DICT["data"]["mvr_reports"]["report_provided_by"] = re.findall(r'Report Provided By : [\w]+', i)[0].split(" ")[1]
    RESP_DICT["data"]["mvr_reports"]["customer"] = re.findall(r'Ordered for: [\w]+', i)[0].split(" ")[1]
    RESP_DICT["data"]["mvr_reports"]["actor"] = None
    RESP_DICT["data"]["mvr_reports"]["customer_ref"] = re.findall(r'Reference: [\w]+', i)[0].split(" ")[1]
    RESP_DICT["data"]["mvr_reports"]["customer_sub"] = None
    RESP_DICT["data"]["mvr_reports"]["date_completed"] = re.findall(r'Order Date: [\w]+', i)
    RESP_DICT["data"]["mvr_reports"]["first_name"] = re.findall(r'Name: [\w]+',i)[0].split(" ")[1]
    RESP_DICT["data"]["mvr_reports"]["last_name"] = re.findall(r'Name: [\w]+',i)[0].split(" ")[1]
    RESP_DICT["data"]["mvr_reports"]["license_no"] = re.findall(r'License: [\w]+',i)[0].split(" ")[1]
    RESP_DICT["data"]["mvr_reports"]["state"] = re.findall(r'state: [\w]+', i)[0].split(" ")[1]
    RESP_DICT["data"]["mvr_driver_reports"]["driver_name"] = re.findall(r'Name: [\w] [ \w]', i)[0].split(" ")[1]
    RESP_DICT["data"]["mvr_driver_reports"]["social_sec_no"] = None
    RESP_DICT["data"]["mvr_driver_reports"]["dob"] = re.findall(r'DOB: [\w]', i)[0].split(" ")[1]

    RESP_DICT["data"]["mvr_driver_license"][f"{j}"]["license"] = re.findall(r'License: [\w]', i)[0].split(" ")[1]
    RESP_DICT["data"]["mvr_driver_license"][f"{j}"]["license_state"] = None
    RESP_DICT["data"]["mvr_driver_license"][f"{j}"]["issue"] = re.findall(r'Issue: [\w]+', i)[0].split(" ")[1]
    RESP_DICT["data"]["mvr_driver_license"][f"{j}"]["expires"] = re.findall(r'Expire: [\w]+', i)[0].split(" ")[1]
    RESP_DICT["data"]["mvr_driver_license"][f"{j}"]["status"] = re.findall(r'Status [\w]+', i)[0].split(" ")[1]
    RESP_DICT["data"]["mvr_driver_license"][f"{j}"]["class"] = re.findall(r'Class [\w]+', i)[0].split(" ")[1]
    RESP_DICT["data"]["mvr_driver_license"][f"{j}"]["restrictions"] = None

    RESP_DICT["data"]["violations"]=None

    RESP_DICT["data"]["actions"][f"{j}"]["type"] = None
    RESP_DICT["data"]["actions"][f"{j}"]["order_date"] = None
    RESP_DICT["data"]["actions"][f"{j}"]["start_date"] = None
    RESP_DICT["data"]["actions"][f"{j}"]["thru_date"] = None
    RESP_DICT["data"]["actions"][f"{j}"]["end_date"] = None
    RESP_DICT["data"]["actions"][f"{j}"]["sp"] = None
    RESP_DICT["data"]["actions"][f"{j}"]["code"] = None
    RESP_DICT["data"]["actions"][f"{j}"]["acd"] = None
    RESP_DICT["data"]["actions"][f"{j}"]["description"]= None

    RESP_DICT["data"]["cdl"]["med_status"] = re.findall(r'Med Status: [\w]+', i)[0].split(" ")[1]
    RESP_DICT["data"]["cdl"]["cert_status"] = re.findall(r'Cert Status:: [\w]+', i)[0].split(" ")[1]
    RESP_DICT["data"]["cdl"]["issue_date"] = re.findall(r'Issued: [\w]+', i)[0].split(" ")[1]
    RESP_DICT["data"]["cdl"]["expiry_date"] = re.findall(r'Expires: [\w]+', i)[0].split(" ")[1]
    RESP_DICT["data"]["cdl"]["cert_date"] = None
    RESP_DICT["data"]["cdl"]["posted_date"] = re.findall(r'Posted Date: [\w]+', i)[0].split(" ")[1]
    RESP_DICT["data"]["cdl"]["examiner"] = re.findall(r'Examiner: [\w]+', i)[0].split(" ")[1]
    RESP_DICT["data"]["cdl"]["examiner_phone"] = re.findall(r'Examiner Phone: [\w]+', i)[0].split(" ")[1]
    RESP_DICT["data"]["cdl"]["juris"] = re.findall(r'Juris: [\w]+', i)[0].split(" ")[1]
    RESP_DICT["data"]["cdl"]["examiner_lic"] = re.findall(r'Examiner Lic: [\w]+', i)[0].split(" ")[1]
    RESP_DICT["data"]["cdl"]["examiner_regno"]= re.findall(r'Examiner Reg Num: [\w]+', i)[0].split(" ")[1]
    RESP_DICT["data"]["cdl"]["examiner_type"] = re.findall(r'Examiner Type: [\w]+', i)[0].split(" ")[1]
    RESP_DICT["data"]["cdl"]["restrictions"] = None

    RESP_DICT["message"] = "Success"
    RESP_DICT["status"]["created_at"]= "23-August-2022 18:10:11"
    RESP_DICT["status"]["statusCode"] = 2001
    RESP_DICT["status"]["statusMessage"] = "Data Extraction successfull."

    return RESP_DICT