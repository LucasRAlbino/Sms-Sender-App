unit u_Main;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.StdCtrls, CPort,
  Vcl.Imaging.pngimage, Vcl.ExtCtrls, Vcl.Buttons;

type
  TfrmMain = class(TForm)
    ComPort1: TComPort;
    ComDataPacket1: TComDataPacket;
    edt_Celular: TEdit;
    Image1: TImage;
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    button: TImage;
    SpeedButton2: TSpeedButton;
    Mem_Msg: TMemo;
    procedure SpeedButton2Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  frmMain: TfrmMain;

implementation

{$R *.dfm}



procedure TfrmMain.SpeedButton2Click(Sender: TObject);
begin
 ComPort1.WriteStr(edt_Celular.Text+'$'+Mem_Msg.Text);
 ShowMessage('Mandei...');

 Mem_Msg.Lines.Clear;
 edt_Celular.Text := '';

 edt_Celular.SetFocus;

end;

end.
