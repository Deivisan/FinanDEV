/**
 * FinanDEV Dashboard - Frontend Logic
 * Criado: 16/11/2025
 * Autor: Deivison Santana (@DeiviTech)
 */

// === Config ===
const API_BASE_URL = 'http://localhost:8000';
const MOCK_MODE = true; // Trocar para false quando backend estiver pronto

// === Data Mock (Temporário) ===
const mockData = {
    weight: {
        current: 60, // [A EDITAR]
        goal: 70,
        lastUpdate: '16/11/2025'
    },
    nutrition: {
        caloriesGoal: 2400,
        proteinGoal: 100,
        meals: 5,
        water: 0 // [A TRACKEAR]
    },
    finance: {
        salary: 1866.53,
        fixedExpenses: 780.00,
        monthlyBalance: 1086.54,
        biweeklyBudget: 250.00,
        actualSpending: 174.40,
        savings: 75.60
    },
    sleep: {
        hoursLastNight: null, // [AUTO-INFERIR]
        quality: null,
        moodToday: null
    },
    tasks: [
        { id: 1, text: 'Testar 5 GCam ports Poco X5', done: false },
        { id: 2, text: 'Capturar 20-30 fotos rosto', done: false },
        { id: 3, text: 'Implementar email-cleanup.py', done: false },
        { id: 4, text: 'Preencher Ambiente-Dev/PC/', done: false },
        { id: 5, text: 'Organizar Google Photos álbuns', done: false }
    ],
    git: {
        commitsWeek: 4,
        linesAdded: 4538,
        filesChanged: 10,
        lastMessage: 'feat: ambiente-dev completo + 7 sistemas nova conversa (166 msgs)'
    },
    lastUpdate: new Date().toLocaleString('pt-BR')
};

// === Init on Page Load ===
document.addEventListener('DOMContentLoaded', () => {
    console.log('🧠 FinanDEV Dashboard inicializado');
    
    if (MOCK_MODE) {
        console.warn('⚠️ MOCK MODE ativo - dados hardcoded');
        loadMockData();
    } else {
        loadRealData();
    }
});

// === Load Mock Data ===
function loadMockData() {
    // Header stats
    document.getElementById('last-update').textContent = mockData.lastUpdate;
    document.getElementById('commits-week').textContent = mockData.git.commitsWeek;
    
    // Card 1: Peso
    document.getElementById('current-weight').textContent = `${mockData.weight.current}kg`;
    const progress = ((mockData.weight.current - 60) / (mockData.weight.goal - 60)) * 100;
    document.getElementById('weight-progress').style.width = `${progress}%`;
    document.getElementById('weight-percent').textContent = 
        `${progress.toFixed(0)}% (${mockData.weight.current - 60}/${mockData.weight.goal - 60}kg)`;
    
    // Card 6: Git
    document.getElementById('commits-count').textContent = mockData.git.commitsWeek;
    
    console.log('✅ Mock data carregado');
}

// === Load Real Data from API ===
async function loadRealData() {
    try {
        console.log('🔄 Carregando dados reais da API...');
        
        const response = await fetch(`${API_BASE_URL}/metrics`);
        if (!response.ok) throw new Error('API error');
        
        const data = await response.json();
        
        // Atualizar UI com dados reais
        // [A IMPLEMENTAR quando backend estiver pronto]
        
        console.log('✅ Dados reais carregados:', data);
    } catch (error) {
        console.error('❌ Erro ao carregar dados:', error);
        alert('Erro ao conectar com API. Verifique se o backend está rodando.');
    }
}

// === Quick Actions ===
function addWeight() {
    const weight = prompt('Digite seu peso atual (kg):');
    if (weight && !isNaN(weight)) {
        console.log(`⚖️ Peso registrado: ${weight}kg`);
        // [A IMPLEMENTAR] Salvar em Vida-Deivison.json via API
        alert(`Peso ${weight}kg registrado! (Mock - não salvo ainda)`);
        
        // Update UI
        document.getElementById('current-weight').textContent = `${weight}kg`;
    }
}

function addMood() {
    const mood = prompt('Como você está hoje? (1=Péssimo, 5=Excelente):');
    if (mood && mood >= 1 && mood <= 5) {
        console.log(`😊 Humor registrado: ${mood}/5`);
        // [A IMPLEMENTAR] Salvar em SAUDE-MENTAL.md via API
        alert(`Humor ${mood}/5 registrado! (Mock - não salvo ainda)`);
        
        // Update UI
        document.getElementById('mood-today').textContent = `${mood}/5`;
    }
}

function addTask() {
    const task = prompt('Nova tarefa:');
    if (task && task.trim() !== '') {
        console.log(`✅ Tarefa adicionada: ${task}`);
        // [A IMPLEMENTAR] Adicionar em Pendencias/ via API
        alert(`Tarefa "${task}" adicionada! (Mock - não salva ainda)`);
        
        // Update UI mock
        mockData.tasks.push({
            id: mockData.tasks.length + 1,
            text: task,
            done: false
        });
    }
}

function quickCommit() {
    const message = prompt('Mensagem do commit:');
    if (message && message.trim() !== '') {
        console.log(`🚀 Commit rápido: ${message}`);
        // [A IMPLEMENTAR] Git commit via script Python
        alert(`Commit "${message}" executado! (Mock - não commitado ainda)`);
    }
}

// === Card Actions ===
function viewTimeline() {
    alert('Timeline de fotos (A IMPLEMENTAR)');
    // [A IMPLEMENTAR] Modal com carrossel fotos progresso
}

function uploadPhoto() {
    alert('Upload de foto (A IMPLEMENTAR)');
    // [A IMPLEMENTAR] Input file + salvar em assets/photos/
}

function addMeal() {
    alert('Registrar refeição (A IMPLEMENTAR)');
    // [A IMPLEMENTAR] Form calorias + proteínas
}

function viewMenu() {
    alert('Cardápio semanal (A IMPLEMENTAR)');
    // [A IMPLEMENTAR] Renderizar Rotinas/Diarias/
}

function addExpense() {
    const expense = prompt('Gasto (R$):');
    const category = prompt('Categoria (ex: alimentação, transporte):');
    if (expense && !isNaN(expense) && category) {
        console.log(`💰 Gasto registrado: R$ ${expense} (${category})`);
        alert(`Gasto R$ ${expense} em "${category}" registrado! (Mock)`);
    }
}

function viewExtract() {
    alert('Extrato financeiro (A IMPLEMENTAR)');
    // [A IMPLEMENTAR] Tabela gastos quinzenais
}

function addTrigger() {
    const trigger = prompt('Gatilho emocional:');
    if (trigger && trigger.trim() !== '') {
        console.log(`⚠️ Gatilho registrado: ${trigger}`);
        alert(`Gatilho "${trigger}" registrado! (Mock)`);
    }
}

function viewAllTasks() {
    alert('Todas as tarefas (A IMPLEMENTAR)');
    // [A IMPLEMENTAR] Modal lista completa Pendencias/
}

function viewRoadmap() {
    alert('Roadmap (A IMPLEMENTAR)');
    // [A IMPLEMENTAR] Renderizar roadmap-mudancas-novembro.md
}

function comparePhotos() {
    alert('Comparar fotos (A IMPLEMENTAR)');
    // [A IMPLEMENTAR] Side-by-side fotos timeline
}

// === Chart.js Initialization (Quando integrar) ===
// function initCharts() {
//     // Nutrition Chart
//     const nutritionCtx = document.getElementById('nutrition-chart').getContext('2d');
//     new Chart(nutritionCtx, {
//         type: 'bar',
//         data: {
//             labels: ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom'],
//             datasets: [{
//                 label: 'Calorias',
//                 data: [2400, 2350, 2420, 2380, 2410, 2300, 2450],
//                 backgroundColor: 'rgba(0, 255, 136, 0.5)'
//             }, {
//                 label: 'Proteínas (g)',
//                 data: [100, 98, 105, 102, 110, 95, 108],
//                 backgroundColor: 'rgba(0, 136, 255, 0.5)'
//             }]
//         }
//     });
// 
//     // Sleep Chart
//     const sleepCtx = document.getElementById('sleep-chart').getContext('2d');
//     new Chart(sleepCtx, {
//         type: 'line',
//         data: {
//             labels: ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom'],
//             datasets: [{
//                 label: 'Horas de Sono',
//                 data: [7, 6.5, 7.5, 6, 8, 9, 7],
//                 borderColor: '#00ff88',
//                 tension: 0.4
//             }]
//         }
//     });
// 
//     // Finance Chart
//     const financeCtx = document.getElementById('finance-chart').getContext('2d');
//     new Chart(financeCtx, {
//         type: 'pie',
//         data: {
//             labels: ['Alimentação', 'Transporte', 'Lazer', 'Economia'],
//             datasets: [{
//                 data: [174.40, 50, 25.60, 75.60],
//                 backgroundColor: ['#ff4444', '#ffaa00', '#00aaff', '#00ff88']
//             }]
//         }
//     });
// 
//     // Commits Heatmap (placeholder)
//     // [A IMPLEMENTAR com canvas customizado ou lib específica]
// }

// === Utility Functions ===
function formatCurrency(value) {
    return new Intl.NumberFormat('pt-BR', {
        style: 'currency',
        currency: 'BRL'
    }).format(value);
}

function formatDate(date) {
    return new Date(date).toLocaleDateString('pt-BR');
}

// === Debug ===
console.log('📊 Mock Data:', mockData);
