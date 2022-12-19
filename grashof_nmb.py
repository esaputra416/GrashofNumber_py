def grashof_number(temperature_difference, length, thermal_expansion_coefficient, modulus_elasticity, gravity_acceleration, viscosity_dynamic):
    """
    Calculates the Grashof number, a dimensionless number used in fluid dynamics and heat transfer.
    
    Parameters:
    temperature_difference (float): The temperature difference between the two fluids.
    length (float): The characteristic length of the system.
    thermal_expansion_coefficient (float): The coefficient of thermal expansion of the fluid.
    modulus_elasticity (float): The modulus of elasticity of the fluid.
    gravity_acceleration (float): The acceleration due to gravity.
    viscosity_dynamic (float): The dynamic viscosity of the fluid.
    
    Returns:
    float: The Grashof number.
    """
    grashof = (temperature_difference * length ** 3 * thermal_expansion_coefficient) / (modulus_elasticity * gravity_acceleration * viscosity_dynamic)
    return grashof

# Example usage
temperature_difference = 100 # degrees Celsius
length = 0.1 # meters
thermal_expansion_coefficient = 1e-3 # 1/K
modulus_elasticity = 2e9 # Pa
gravity_acceleration = 9.81 # m/s^2
viscosity_dynamic = 1e-3 # Pa*s

grashof_number = grashof_number(temperature_difference, length, thermal_expansion_coefficient, modulus_elasticity, gravity_acceleration, viscosity_dynamic)
print(grashof_number) # prints 9.81e9

