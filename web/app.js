// SendBack Web App
const API_BASE = 'http://localhost:5000/api';

// DOM Elements
const merchantSearch = document.getElementById('merchantSearch');
const searchBtn = document.getElementById('searchBtn');
const searchResults = document.getElementById('searchResults');
const uploadArea = document.getElementById('uploadArea');
const fileInput = document.getElementById('fileInput');
const textInput = document.getElementById('textInput');
const parseTextBtn = document.getElementById('parseTextBtn');
const resultsSection = document.getElementById('resultsSection');
const resetBtn = document.getElementById('resetBtn');
const merchantsList = document.getElementById('merchantsList');

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    setupEventListeners();
    loadMerchants();
});

function setupEventListeners() {
    // Merchant search
    searchBtn.addEventListener('click', handleMerchantSearch);

    merchantSearch.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            handleMerchantSearch();
        }
    });

    // File upload
    uploadArea.addEventListener('click', () => fileInput.click());

    fileInput.addEventListener('change', (e) => {
        if (e.target.files.length > 0) {
            handleFileUpload(e.target.files[0]);
        }
    });

    // Drag and drop
    uploadArea.addEventListener('dragover', (e) => {
        e.preventDefault();
        uploadArea.classList.add('dragover');
    });

    uploadArea.addEventListener('dragleave', () => {
        uploadArea.classList.remove('dragover');
    });

    uploadArea.addEventListener('drop', (e) => {
        e.preventDefault();
        uploadArea.classList.remove('dragover');

        if (e.dataTransfer.files.length > 0) {
            handleFileUpload(e.dataTransfer.files[0]);
        }
    });

    // Text parsing
    parseTextBtn.addEventListener('click', handleTextParse);

    // Reset
    resetBtn.addEventListener('click', resetForm);
}

async function handleMerchantSearch() {
    const query = merchantSearch.value.trim();

    if (!query) {
        alert('Please enter a merchant name');
        return;
    }

    searchBtn.disabled = true;
    searchBtn.textContent = 'Searching...';
    searchResults.style.display = 'none';

    try {
        const response = await fetch(`${API_BASE}/search?q=${encodeURIComponent(query)}`);
        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || 'Search failed');
        }

        displaySearchResults(data.results, query);

    } catch (error) {
        alert('Error searching: ' + error.message);
    } finally {
        searchBtn.disabled = false;
        searchBtn.textContent = 'Search';
    }
}

function displaySearchResults(results, query) {
    searchResults.style.display = 'block';

    if (results.length === 0) {
        searchResults.innerHTML = `
            <div class="no-results">
                <p>No results found for "${query}"</p>
                <p>Try searching for: Amazon, Nike, Apple, Walmart, Target, etc.</p>
            </div>
        `;
        return;
    }

    let html = `<p style="color: var(--text-light); margin-bottom: 24px; font-size: 15px;">
        Found ${results.length} result${results.length > 1 ? 's' : ''} for "<strong style="color: var(--text);">${query}</strong>"
    </p>`;

    results.forEach((merchant, index) => {
        const itemId = `search-item-${index}`;
        const addressId = `address-${index}`;

        html += `
            <div class="search-result-item" id="${itemId}">
                <div class="search-result-header">
                    <h3>${merchant.name}</h3>
                    ${merchant.free_return_label ? '<span class="search-result-badge">✓ Free Label</span>' : ''}
                </div>

                <div class="search-result-details">
                    <div class="search-result-detail">
                        <strong>Return Window</strong>
                        ${merchant.return_window_days} days
                    </div>
                    <div class="search-result-detail">
                        <strong>Customer Service</strong>
                        ${merchant.customer_service}
                    </div>
                </div>

                <div class="search-result-actions">
                    ${merchant.return_portal_url ? `
                        <a href="${merchant.return_portal_url}" target="_blank" class="btn">
                            Get Free Return Label →
                        </a>
                    ` : ''}
                    <button class="btn" onclick="toggleAddress('${addressId}')">
                        Show Return Address
                    </button>
                </div>

                <div class="search-result-address" id="${addressId}">
                    <strong style="display: block; margin-bottom: 0.5rem;">RETURN ADDRESS:</strong>
                    ${merchant.return_address}

                    <div style="margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255, 255, 255, 0.2);">
                        <strong style="display: block; margin-bottom: 0.5rem;">INSTRUCTIONS:</strong>
                        ${merchant.instructions}
                    </div>
                </div>
            </div>
        `;
    });

    searchResults.innerHTML = html;
}

function toggleAddress(addressId) {
    const addressDiv = document.getElementById(addressId);
    if (addressDiv) {
        addressDiv.classList.toggle('visible');
    }
}

async function handleFileUpload(file) {
    // Validate file
    const allowedTypes = ['application/pdf', 'image/png', 'image/jpeg', 'image/jpg', 'text/plain'];
    if (!allowedTypes.includes(file.type)) {
        alert('Please upload a PDF, image, or text file');
        return;
    }

    // Show loading
    uploadArea.innerHTML = '<div class="loading">Processing file...</div>';

    try {
        const formData = new FormData();
        formData.append('file', file);

        const response = await fetch(`${API_BASE}/parse`, {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error('Failed to parse file');
        }

        const data = await response.json();
        displayResults(data);

    } catch (error) {
        alert('Error processing file: ' + error.message);
        resetUploadArea();
    }
}

async function handleTextParse() {
    const text = textInput.value.trim();

    if (!text) {
        alert('Please paste your order confirmation text');
        return;
    }

    parseTextBtn.disabled = true;
    parseTextBtn.textContent = 'Processing...';

    try {
        const response = await fetch(`${API_BASE}/parse/text`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text })
        });

        if (!response.ok) {
            throw new Error('Failed to parse text');
        }

        const data = await response.json();
        displayResults(data);

    } catch (error) {
        alert('Error processing text: ' + error.message);
    } finally {
        parseTextBtn.disabled = false;
        parseTextBtn.textContent = 'Parse Text';
    }
}

function displayResults(data) {
    const { parsed, merchant_info, days_remaining } = data;

    // Show results section
    resultsSection.style.display = 'block';

    // Display order details
    const orderDetails = document.getElementById('orderDetails');
    orderDetails.innerHTML = '';

    if (parsed.merchant) {
        addDetailItem(orderDetails, 'Merchant', parsed.merchant.toUpperCase());
    }

    if (parsed.order_number) {
        addDetailItem(orderDetails, 'Order Number', parsed.order_number);
    }

    if (parsed.order_date) {
        const date = new Date(parsed.order_date);
        addDetailItem(orderDetails, 'Order Date', date.toLocaleDateString());
    }

    if (parsed.return_by_date) {
        const returnDate = new Date(parsed.return_by_date);
        let className = 'good';
        if (days_remaining < 7) className = 'urgent';
        else if (days_remaining < 14) className = 'warning';

        addDetailItem(
            orderDetails,
            'Return By',
            `${returnDate.toLocaleDateString()} (${days_remaining} days left)`,
            className
        );
    }

    if (parsed.total) {
        addDetailItem(orderDetails, 'Total', parsed.total);
    }

    // Display merchant return info
    if (merchant_info) {
        displayMerchantInfo(merchant_info);
    } else {
        document.getElementById('returnInfoGroup').style.display = 'none';
        document.getElementById('addressGroup').style.display = 'none';
        document.getElementById('instructionsGroup').style.display = 'none';

        // Show extracted address if available
        if (parsed.extracted_return_address) {
            const addressGroup = document.getElementById('addressGroup');
            addressGroup.style.display = 'block';
            document.getElementById('returnAddress').textContent = parsed.extracted_return_address;
        }
    }

    // Scroll to results
    resultsSection.scrollIntoView({ behavior: 'smooth' });
}

function displayMerchantInfo(merchantInfo) {
    // Return info
    const returnInfoGroup = document.getElementById('returnInfoGroup');
    const returnInfo = document.getElementById('returnInfo');
    returnInfoGroup.style.display = 'block';

    let infoHTML = '<div class="info-box">';

    if (merchantInfo.free_return_label) {
        infoHTML += '<p><strong>✅ Free Return Label Available</strong></p>';
    } else {
        infoHTML += '<p><strong>⚠️ Return label policy varies</strong></p>';
    }

    infoHTML += `<p>Return Window: ${merchantInfo.return_window_days} days</p>`;
    infoHTML += `<p>Customer Service: ${merchantInfo.customer_service}</p>`;
    infoHTML += '</div>';

    if (merchantInfo.return_portal_url) {
        infoHTML += `<a href="${merchantInfo.return_portal_url}" target="_blank" class="portal-link">
            Open Return Portal →
        </a>`;
    }

    returnInfo.innerHTML = infoHTML;

    // Return address
    const addressGroup = document.getElementById('addressGroup');
    const returnAddress = document.getElementById('returnAddress');
    addressGroup.style.display = 'block';
    returnAddress.textContent = merchantInfo.return_address;

    // Instructions
    const instructionsGroup = document.getElementById('instructionsGroup');
    const instructions = document.getElementById('instructions');
    instructionsGroup.style.display = 'block';

    let instructionsHTML = `<p>${merchantInfo.instructions}</p>`;

    if (merchantInfo.return_portal_url) {
        instructionsHTML += `
            <ol class="steps-list">
                <li>
                    <strong>Visit Return Portal</strong>
                    <p>Go to ${merchantInfo.name}'s official return portal</p>
                </li>
                <li>
                    <strong>Log In</strong>
                    <p>Sign in with your account credentials</p>
                </li>
                <li>
                    <strong>Select Order</strong>
                    <p>Find your order in order history</p>
                </li>
                <li>
                    <strong>Request Return</strong>
                    <p>Select items to return and reason</p>
                </li>
                ${merchantInfo.free_return_label ? `
                <li>
                    <strong>Print Label</strong>
                    <p>Download and print prepaid return label</p>
                </li>
                ` : ''}
                <li>
                    <strong>Pack & Ship</strong>
                    <p>Pack securely, attach label, drop off at carrier</p>
                </li>
            </ol>
        `;
    }

    instructions.innerHTML = instructionsHTML;
}

function addDetailItem(container, label, value, className = '') {
    const item = document.createElement('div');
    item.className = 'detail-item';

    item.innerHTML = `
        <div class="detail-label">${label}</div>
        <div class="detail-value ${className}">${value}</div>
    `;

    container.appendChild(item);
}

async function loadMerchants() {
    try {
        const response = await fetch(`${API_BASE}/merchants`);
        const data = await response.json();

        merchantsList.innerHTML = '';

        data.merchants.forEach(merchant => {
            const card = document.createElement('div');
            card.className = 'merchant-card';

            card.innerHTML = `
                <h4>${merchant.name}</h4>
                <p style="font-size: 0.85rem; color: var(--text-light);">
                    ${merchant.return_window_days} day returns
                </p>
                ${merchant.free_label ? '<span class="badge">Free Label</span>' : ''}
            `;

            merchantsList.appendChild(card);
        });

    } catch (error) {
        merchantsList.innerHTML = '<div class="loading">Failed to load merchants</div>';
    }
}

function resetForm() {
    resultsSection.style.display = 'none';
    textInput.value = '';
    fileInput.value = '';
    resetUploadArea();
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function resetUploadArea() {
    uploadArea.innerHTML = `
        <div class="upload-content">
            <svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                <polyline points="17 8 12 3 7 8"></polyline>
                <line x1="12" y1="3" x2="12" y2="15"></line>
            </svg>
            <p>Click to upload or drag & drop</p>
            <p class="small">PDF, PNG, JPG, or TXT</p>
        </div>
    `;
}
