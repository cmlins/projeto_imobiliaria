import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListarImoveisComponent } from './listar-imoveis.component';

describe('ListarImoveisComponent', () => {
  let component: ListarImoveisComponent;
  let fixture: ComponentFixture<ListarImoveisComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ListarImoveisComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ListarImoveisComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
