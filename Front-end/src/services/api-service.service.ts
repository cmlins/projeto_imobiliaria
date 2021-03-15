import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class ApiServiceService {

  constructor(private httpClient: HttpClient) { }
  // MÉTODOS DE IMÓVEIS
  public getImoveis(){
    return this.httpClient.get(`http://127.0.0.1:5000/Imoveis/`);
  }
  public getImovel(id:any){
    return this.httpClient.get(`http://127.0.0.1:5000/Imoveis/${id}`);
  }
  public postImovel(imovel:any){
    return this.httpClient.post(`http://127.0.0.1:5000/Imoveis`, imovel);
  }
  // MÉTODOS DE PESSOAS
  public getPessoas(){
    return this.httpClient.get(`http://127.0.0.1:5000/Pessoas/`);
  }
  public getPessoa(id:any){
    return this.httpClient.get(`http://127.0.0.1:5000/Pessoas/${id}`);
  }
  public postPessoa(pessoa:any){
    return this.httpClient.post(`http://127.0.0.1:5000/Clientes`, pessoa);
  }
  // MÉTODOS DE CLIENTE
  public getClientes(){
    return this.httpClient.get(`http://127.0.0.1:5000/Clientes/`);
  }
  public getCliente(id:any){
    return this.httpClient.get(`http://127.0.0.1:5000/Clientes/${id}`);
  }
  public postCliente(cliente:any){
    return this.httpClient.post(`http://127.0.0.1:5000/Clientes`, cliente);
  }
  // MÉTODOS DE ENDEREÇO
  public getEndereços(){
    return this.httpClient.get(`http://127.0.0.1:5000/Endereços/`);
  }
  public getEndereço(id:any){
    return this.httpClient.get(`http://127.0.0.1:5000/Endereços/${id}`);
  }
  public postEndereço(endereco:any){
    return this.httpClient.post(`http://127.0.0.1:5000/Endereços`, endereco);
  }
  public getTipos(){
    return this.httpClient.get(`http://127.0.0.1:5000/Imoveis/tipo`);
  }
  public getGastos(){
    return this.httpClient.get(`http://127.0.0.1:5000/Imoveis/gastos`);
  }
}
