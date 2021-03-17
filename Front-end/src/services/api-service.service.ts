import { EventEmitter, Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class ApiService {

  enviarDadosImovel = new EventEmitter<any>();

  constructor(private httpClient: HttpClient) { }

  public getImoveis(){
    return this.httpClient.get(`http://127.0.0.1:5000/Imoveis/`);
  }

  public getImovel(id:any){
    return this.httpClient.get(`http://127.0.0.1:5000/Imoveis/${id}`);
  }

  public getPessoas(){
    return this.httpClient.get(`http://127.0.0.1:5000/Pessoas/`);
  }
  public getPessoa(id:any){
    return this.httpClient.get(`http://127.0.0.1:5000/Pessoas/${id}`);
  }

  public getClientes(){
    return this.httpClient.get(`http://127.0.0.1:5000/Clientes/`);
  }

  public getCliente(id:any){
    return this.httpClient.get(`http://127.0.0.1:5000/Clientes/${id}`);
  }

  public getEndereços(){
    return this.httpClient.get(`http://127.0.0.1:5000/Endereco/`);
  }

  public getEndereço(id:any){
    return this.httpClient.get(`http://127.0.0.1:5000/Endereco/${id}`);
  }

  public getTipos(){
    return this.httpClient.get(`http://127.0.0.1:5000/Imoveis/tipo`);
  }

  public getGastos(){
    return this.httpClient.get(`http://127.0.0.1:5000/Imoveis/gastos`);
  }

  public postEndereço(endereco:any){
    return this.httpClient.post(`http://127.0.0.1:5000/Endereco/`, endereco);
  }

  public postCliente(cliente:any){
    return this.httpClient.post(`http://127.0.0.1:5000/Clientes/`, cliente);
  }

  public postPessoa(pessoa:any){
    return this.httpClient.post(`http://127.0.0.1:5000/Pessoas/`, pessoa);
  }

  public postImovel(imovel:any){
    return this.httpClient.post(`http://127.0.0.1:5000/Imoveis/`, imovel);
  }

  public postTransacao(transacao:any){
    return this.httpClient.post(`http://127.0.0.1:5000/Transacoes/`, transacao);
  }
}
