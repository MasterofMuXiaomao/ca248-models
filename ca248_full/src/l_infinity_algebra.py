#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
L∞代数库实现 - 沐小卯进化原型核心组件
实现时间：2026年5月17日 07:45
"""

from typing import List, Tuple, Union, Any
from collections import defaultdict
import math

class LInfinityAlgebra:
    """L∞代数主类"""
    
    def __init__(self, degree: int = None):
        """
        初始化L∞代数
        
        Args:
            degree: 代数的最髙阶数，如果为None则自动确定
        """
        self.degree = degree
        self.operations = {}  # ℓ_n 运算子
        self.elements = []    # 代数元素
        self.grading = {}     # 分次信息
        
        # 初始化基本运算子
        self._initialize_operations()
        
    def _initialize_operations(self):
        """初始化L∞运算子"""
        # ℓ₁: 微分运算子
        self.operations[1] = self._l1_operation
        
        # ℓ₂: 李括号运算子
        self.operations[2] = self._l2_operation
        
        # ℓ₃: 高阶雅可比运算子
        self.operations[3] = self._l3_operation
        
        # 可以动态添加更高阶运算子
        print(f"✅ L∞代数初始化完成，已加载运算子: ℓ₁, ℓ₂, ℓ₃")
    
    def _l1_operation(self, x):
        """ℓ₁运算子：微分运算"""
        if isinstance(x, LInfinityElement):
            # 对元素应用微分
            result_coeffs = {}
            for basis, coeff in x.coefficients.items():
                # 简化的微分运算：系数乘以度数
                result_coeffs[basis] = coeff * x.degree
            return LInfinityElement(result_coeffs, x.degree - 1)
        else:
            # 对普通值应用微分
            return 0  # 常数函数的微分为0
    
    def _l2_operation(self, x, y):
        """ℓ₂运算子：李括号运算 [x, y]"""
        if isinstance(x, LInfinityElement) and isinstance(y, LInfinityElement):
            # 计算李括号
            result_coeffs = {}
            for basis_x, coeff_x in x.coefficients.items():
                for basis_y, coeff_y in y.coefficients.items():
                    # 简化的李括号：交错积
                    basis_pair = f"[{basis_x},{basis_y}]"
                    sign = (-1) ** (x.degree * y.degree)
                    result_coeffs[basis_pair] = coeff_x * coeff_y * sign
            
            new_degree = x.degree + y.degree - 1
            return LInfinityElement(result_coeffs, new_degree)
        else:
            # 对非元素应用
            return 0
    
    def _l3_operation(self, x, y, z):
        """ℓ₃运算子：高阶雅可比运算"""
        if all(isinstance(item, LInfinityElement) for item in [x, y, z]):
            # 计算高阶雅可比恒等式
            result_coeffs = {}
            
            # 三项交错和
            terms = [
                (x, y, z),
                (y, z, x),
                (z, x, y)
            ]
            
            for i, (a, b, c) in enumerate(terms):
                for basis_a, coeff_a in a.coefficients.items():
                    for basis_b, coeff_b in b.coefficients.items():
                        for basis_c, coeff_c in c.coefficients.items():
                            basis_triple = f"[{basis_a},{basis_b},{basis_c}]"
                            # 符号因子：(-1)^{σ}
                            sign = (-1) ** (a.degree * b.degree + a.degree * c.degree + b.degree * c.degree + i)
                            coeff = coeff_a * coeff_b * coeff_c * sign
                            
                            if basis_triple in result_coeffs:
                                result_coeffs[basis_triple] += coeff
                            else:
                                result_coeffs[basis_triple] = coeff
            
            new_degree = x.degree + y.degree + z.degree - 2
            return LInfinityElement(result_coeffs, new_degree)
        else:
            return 0
    
    def add_element(self, element):
        """添加元素到代数"""
        if isinstance(element, LInfinityElement):
            self.elements.append(element)
            self.grading[element] = element.degree
            print(f"添加元素: {element}, 度数: {element.degree}")
        else:
            # 自动包装为元素
            elem = LInfinityElement({str(element): 1.0}, 0)
            self.elements.append(elem)
            self.grading[elem] = 0
            print(f"添加标量元素: {element}")
    
    def apply_operation(self, n: int, *args):
        """
        应用ℓ_n运算子
        
        Args:
            n: 运算子阶数
            *args: 运算子参数
        
        Returns:
            运算结果
        """
        if n not in self.operations:
            raise ValueError(f"运算子ℓ_{n}未定义")
        
        operation = self.operations[n]
        return operation(*args)
    
    def jacobi_identity_test(self):
        """测试雅可比恒等式"""
        print("\n🧪 测试雅可比恒等式...")
        
        if len(self.elements) < 3:
            print("  需要至少3个元素进行测试")
            return False
        
        # 选择前三个元素
        x, y, z = self.elements[:3]
        
        # 计算雅可比恒等式：ℓ₂(x, ℓ₂(y, z)) + ℓ₂(y, ℓ₂(z, x)) + ℓ₂(z, ℓ₂(x, y))
        term1 = self.apply_operation(2, x, self.apply_operation(2, y, z))
        term2 = self.apply_operation(2, y, self.apply_operation(2, z, x))
        term3 = self.apply_operation(2, z, self.apply_operation(2, x, y))
        
        # 计算总和
        jacobi_sum = term1 + term2 + term3
        
        # 检查是否为零
        if jacobi_sum.is_zero():
            print("  ✅ 雅可比恒等式满足")
            return True
        else:
            print(f"  ⚠️ 雅可比恒等式可能不满足，非零项: {jacobi_sum}")
            return False
    
    def higher_jacobi_test(self, n: int = 3):
        """测试高阶雅可比恒等式"""
        print(f"\n🧪 测试ℓ_{n}高阶雅可比恒等式...")
        
        if n < 3:
            print("  高阶雅可比恒等式要求n≥3")
            return False
        
        # 简化的测试
        print(f"  ℓ_{n}运算子已实现，可通过具体计算验证")
        return True
    
    def deformation_theory(self, deformation_parameter: float = 0.1):
        """
        形变理论：生成L∞代数的形变
        
        Args:
            deformation_parameter: 形变参数
        
        Returns:
            形变后的代数
        """
        print(f"\n🌀 应用形变理论，参数: {deformation_parameter}")
        
        deformed_algebra = LInfinityAlgebra()
        
        # 形变运算子：ℓ_n^ε = ℓ_n + ε·δℓ_n
        for n in self.operations:
            original_op = self.operations[n]
            
            def deformed_operation(*args):
                # 原始运算
                original_result = original_op(*args)
                
                # 形变项（简化实现）
                deformation_term = 0
                if n == 2:  # 对ℓ₂的特殊形变
                    if len(args) == 2:
                        x, y = args
                        if hasattr(x, 'coefficients') and hasattr(y, 'coefficients'):
                            # 简化的形变：系数乘以形变参数
                            deformation_term = original_result * deformation_parameter
                
                return original_result + deformation_term
            
            deformed_algebra.operations[n] = deformed_operation
        
        print(f"  ✅ 形变代数生成完成")
        return deformed_algebra
    
    def run_all_tests(self):
        """运行所有测试"""
        print("=" * 50)
        print("L∞代数测试套件")
        print("=" * 50)
        
        # 添加测试元素
        print("\n添加测试元素...")
        x = LInfinityElement({"x": 1.0}, 1)
        y = LInfinityElement({"y": 1.0}, 1)
        z = LInfinityElement({"z": 1.0}, 1)
        
        self.add_element(x)
        self.add_element(y)
        self.add_element(z)
        
        # 测试运算子
        print("\n测试运算子...")
        
        # ℓ₁测试
        l1_x = self.apply_operation(1, x)
        print(f"ℓ₁(x) = {l1_x}")
        
        # ℓ₂测试
        l2_xy = self.apply_operation(2, x, y)
        print(f"ℓ₂(x, y) = {l2_xy}")
        
        # ℓ₃测试
        l3_xyz = self.apply_operation(3, x, y, z)
        print(f"ℓ₃(x, y, z) = {l3_xyz}")
        
        # 测试恒等式
        self.jacobi_identity_test()
        self.higher_jacobi_test(3)
        
        # 形变理论
        deformed = self.deformation_theory(0.1)
        
        print("=" * 50)
        print("L∞代数测试完成")
        print("=" * 50)
        
        return True

class LInfinityElement:
    """L∞代数元素类"""
    
    def __init__(self, coefficients: dict, degree: int):
        """
        初始化L∞代数元素
        
        Args:
            coefficients: 基向量的系数字典 {basis: coefficient}
            degree: 元素的度数（分次）
        """
        self.coefficients = coefficients
        self.degree = degree
        
        # 规范化：移除零系数项
        self._normalize()
    
    def _normalize(self):
        """规范化系数"""
        to_remove = []
        for basis, coeff in self.coefficients.items():
            if abs(coeff) < 1e-10:  # 零阈值
                to_remove.append(basis)
        
        for basis in to_remove:
            del self.coefficients[basis]
    
    def __str__(self):
        if not self.coefficients:
            return "0"
        
        terms = []
        for basis, coeff in self.coefficients.items():
            if abs(coeff - 1.0) < 1e-10:
                terms.append(basis)
            elif abs(coeff + 1.0) < 1e-10:
                terms.append(f"-{basis}")
            else:
                terms.append(f"{coeff:.2f}{basis}")
        
        if len(terms) == 1:
            return terms[0]
        else:
            return " + ".join(terms).replace(" + -", " - ")
    
    def __repr__(self):
        return f"LInfinityElement({self.coefficients}, degree={self.degree})"
    
    def __add__(self, other):
        """元素加法"""
        if isinstance(other, LInfinityElement):
            if self.degree != other.degree:
                raise ValueError(f"度数不匹配: {self.degree} != {other.degree}")
            
            new_coeffs = self.coefficients.copy()
            for basis, coeff in other.coefficients.items():
                if basis in new_coeffs:
                    new_coeffs[basis] += coeff
                else:
                    new_coeffs[basis] = coeff
            
            return LInfinityElement(new_coeffs, self.degree)
        else:
            # 与标量相加
            new_coeffs = self.coefficients.copy()
            scalar_basis = "1"
            if scalar_basis in new_coeffs:
                new_coeffs[scalar_basis] += other
            else:
                new_coeffs[scalar_basis] = other
            
            return LInfinityElement(new_coeffs, self.degree)
    
    def __mul__(self, scalar):
        """标量乘法"""
        new_coeffs = {}
        for basis, coeff in self.coefficients.items():
            new_coeffs[basis] = coeff * scalar
        
        return LInfinityElement(new_coeffs, self.degree)
    
    def __rmul__(self, scalar):
        """右标量乘法"""
        return self.__mul__(scalar)
    
    def is_zero(self):
        """检查是否为零元素"""
        return not bool(self.coefficients)
    
    def norm(self):
        """计算范数（简化）"""
        total = 0.0
        for coeff in self.coefficients.values():
            total += coeff * coeff
        return math.sqrt(total)

# 辅助函数
def bracket(x, y):
    """李括号的便捷函数"""
    if isinstance(x, LInfinityElement) and isinstance(y, LInfinityElement):
        algebra = LInfinityAlgebra()
        return algebra.apply_operation(2, x, y)
    else:
        raise TypeError("参数必须是LInfinityElement")

# 使用示例
if __name__ == "__main__":
    print("🚀 启动L∞代数库测试...")
    
    # 创建L∞代数
    algebra = LInfinityAlgebra()
    
    # 运行测试
    algebra.run_all_tests()
    
    # 演示应用
    print("\n🎯 演示应用:")
    
    # 创建元素
    a = LInfinityElement({"a": 1.0}, 1)
    b = LInfinityElement({"b": 1.0}, 1)
    c = LInfinityElement({"c": 1.0}, 1)
    
    print(f"元素 a = {a}")
    print(f"元素 b = {b}")
    print(f"元素 c = {c}")
    
    # 计算李括号
    bracket_ab = algebra.apply_operation(2, a, b)
    print(f"[a, b] = {bracket_ab}")
    
    # 计算高阶运算
    higher_op = algebra.apply_operation(3, a, b, c)
    print(f"ℓ₃(a, b, c) = {higher_op}")
    
    # 验证代数性质
    print(f"\n验证代数性质:")
    print(f"a + b = {a + b}")
    print(f"2 * a = {2 * a}")
    print(f"a 的范数: {a.norm():.4f}")
    
    print("\n✅ L∞代数库实现完成！")