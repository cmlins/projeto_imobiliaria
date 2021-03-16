import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api-service.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = "Imobiliária Vida Nova"
  isCollapsed = true;

  constructor(private apiService: ApiService) { }

  ngOnInit() {}

}
