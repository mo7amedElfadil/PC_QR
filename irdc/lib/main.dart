import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:barcode_scan/barcode_scan.dart';
import 'package:flutter/services.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() => runApp(MaterialApp(
      home: Home(),
    ));

class Home extends StatefulWidget {
  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  String result = "IRDC Qrcode Scanner";
  String txt;

  List<String> ind =[];

  Future<void> _scanQr() async {

    try {
      ScanResult qrResult = await BarcodeScanner.scan();
      result = qrResult.rawContent;
      await _postPy(result.toString());

      await _getPy();


      setState(() {


        result = txt;

      });

    } on PlatformException catch (ex) {
      if (ex.code == BarcodeScanner.cameraAccessDenied) {
        setState(() {
          result = "Camera permission was denied";
        });
      } else {
        setState(() {
          result = "Unknown Error $ex";
        });
      }
    } on FormatException {
      setState(() {
        result = "There is an error somewhere";
      });
    } catch (ex) {
      setState(() {
        result = "these is $ex";
      });
    }
  }

    Future<void> _getPy() async{
    txt = "test";
    Uri myUri = Uri.parse('http://127.0.0.1:5000/id');
    final response1 = await http.get(myUri);

    final decoded = await json.decode(response1.body) as List<dynamic>;

    setState((){
      txt = decoded[1];

      return txt;
    });

  }

  Future<void> _postPy(result) async{
    Uri myUri = Uri.parse('http://127.0.0.1:5000/id');
    final response2 = await http.post(myUri, body: json.encode({'id': int.parse(result)}));


  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        title: Text(
          'IRDC',
          style: TextStyle(
            color: Colors.blue,
            fontSize: 20,
            fontWeight: FontWeight.bold,
          ),
        ),
        centerTitle: true,
        backgroundColor: Colors.white,
        elevation: 0,
      ),
      body: Center(
        child: Column(
          children: [
            Row(
              children: [
                SizedBox(
                  width: 30.0,
                ),
                Container(
                  height: 300.0,
                  width: 300.0,
                  child: Image(
                    image: AssetImage('assets/irdc-logo.jpg'),
                  ),
                ),
              ],
            ),
            SizedBox(
              height: 20.0,
            ),
            Row(
              children: [
                SizedBox(
                  width: 65.0,
                ),
                SizedBox(
                  width: 340,
                  height: 100,
                  child: Text(
                    '$result   ',
                    style: TextStyle(
                      fontWeight: FontWeight.bold,
                      fontSize: 10.0,
                      color: Colors.blue,
                    ),
                  ),
                ),
              ],
            ),
            SizedBox(
              height: 40.0,
            ),
            Row(
              children: [
                SizedBox(
                  width: 45.0,
                ),
                SizedBox(
                  width: 300.0,
                  height: 50.0,
                  child: OutlineButton(
                      onPressed: _scanQr,
                      child: Text(
                        'scan',
                        style: TextStyle(
                          color: Colors.blue,
                          fontSize: 20.0,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.all(Radius.circular(30)),
                      )),

                )

              ],
            ),
          ],
        ),
      ),
    );
  }
}
