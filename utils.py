import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# 1. Chuẩn hoá dữ liệu (Z-score normalization)
def standardize_data(data):
    return (data - data.mean()) / data.std()
# 2. Kiểm định KMO (Kaiser-Meyer-Olkin)
def kmo_test(data):
    corr_matrix = data.corr().values
    inv_corr_matrix = np.linalg.inv(corr_matrix)
    n = corr_matrix.shape[0]
    
    # Tính phần tử ngoài đường chéo
    partial_corr = -inv_corr_matrix / np.sqrt(np.outer(np.diag(inv_corr_matrix), np.diag(inv_corr_matrix)))
    np.fill_diagonal(partial_corr, 0)
    
    aij2 = np.sum(corr_matrix**2) - np.sum(np.diag(corr_matrix)**2)
    bij2 = np.sum(partial_corr**2)
    
    kmo_value = aij2 / (aij2 + bij2)
    return kmo_value
# 3. Kiểm định Bartlett
def bartlett_test(data):
    from scipy.stats import chi2
    n, p = data.shape
    corr_matrix = data.corr().values
    det_corr = np.linalg.det(corr_matrix)
    
    if det_corr <= 0:
        raise ValueError("Determinant of the correlation matrix is non-positive.")
    
    chi_square_value = -(n - 1 - (2*p + 5)/6) * np.log(det_corr)
    df = p * (p - 1) / 2
    p_value = 1 - chi2.cdf(chi_square_value, df)
    
    return chi_square_value, df, p_value
# 4. Tính giá trị riêng và phương sai tích lũy
def calculate_eigenvalues_and_variance(data):
    corr_matrix = data.corr().values
    eigenvalues, _ = np.linalg.eig(corr_matrix)
    
    # Sắp xếp giá trị riêng giảm dần
    sorted_indices = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[sorted_indices]
    
    # Tính phương sai giải thích và phương sai tích lũy
    variance_explained = (eigenvalues / np.sum(eigenvalues)) * 100
    cumulative_variance = np.cumsum(variance_explained)
    
    return eigenvalues, variance_explained, cumulative_variance

# 5. Tính ma trận hệ số tải, không dùng FactorAnalysis, PCA của sklearn
def factor_loadings(data, num_factors):
    corr_matrix = data.corr().values
    eigenvalues, eigenvectors = np.linalg.eig(corr_matrix)
    
    # Sắp xếp giá trị riêng và vector riêng tương ứng
    sorted_indices = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[sorted_indices]
    eigenvectors = eigenvectors[:, sorted_indices]
    
    # Chọn số vector riêng ứng với số nhân tố cần thiết
    selected_eigenvectors = eigenvectors[:, :num_factors]
    
    # Tính ma trận hệ số tải
    loadings = selected_eigenvectors * np.sqrt(eigenvalues[:num_factors])
    
    # Chuyển ma trận hệ số tải thành DataFrame để dễ đọc
    loadings_df = pd.DataFrame(loadings, index=data.columns, columns=[f'Factor {i+1}' for i in range(num_factors)])
    
    return loadings_df
# 6. Xoay nhân tố (varimax)
def rotate_factors(loadings, method='varimax'):
    from scipy.linalg import svd
    
    if method != 'varimax':
        raise ValueError("Currently only 'varimax' rotation is implemented.")
    
    # Varimax rotation
    def varimax(Phi, gamma=1.0, q=20, tol=1e-6):
        p, k = Phi.shape
        R = np.eye(k)
        d = 0
        for i in range(q):
            d_old = d
            Lambda = np.dot(Phi, R)
            u, s, vh = svd(np.dot(Phi.T, np.asarray(Lambda)**3 - (gamma/p) * np.dot(Lambda, np.diag(np.sum(Lambda**2, axis=0)))))
            R = np.dot(u, vh)
            d = np.sum(s)
            if d_old != 0 and d/d_old < 1 + tol:
                break
        return np.dot(Phi, R)
    
    rotated_loadings = varimax(loadings.values)
    rotated_loadings_df = pd.DataFrame(rotated_loadings, index=loadings.index, columns=loadings.columns)
    
    return rotated_loadings_df
# 7. Tính điểm nhân tố cho từng quan sát
def factor_scores(data, loadings):
    # Chuẩn hóa dữ liệu
    standardized_data = (data - data.mean()) / data.std()
    
    # Tính điểm nhân tố
    scores = np.dot(standardized_data, loadings.values)
    
    scores_df = pd.DataFrame(scores, index=data.index, columns=loadings.columns)
    
    return scores_df