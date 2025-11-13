%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PhysioIndexR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Physiological and Stress Indices for Crop Evaluation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Crop production systems are increasingly challenged by climate
variability, resource limitations, and biotic–abiotic stresses. In this
context, stress tolerance indices and physiological trait estimators are
essential tools to identify stable and superior genotypes, quantify yield
stability under stress versus non-stress conditions, and understand plant
adaptive responses. The 'PhysioIndexR' package provides a unified
framework to compute commonly used stress indices, physiological traits,
and derived metrics that are critical in crop improvement, crop
physiology, and other agricultural sciences. The package includes
functions to calculate classical stress tolerance indices (See Lamba et
al., 2023; <doi:10.1038/s41598-023-37634-8>) such as Tolerance (TOL),
Stress Tolerance Index (STI), Stress Susceptibility Percentage Index
(SSPI), Yield Index (YI), Yield Stability Index (YSI), Relative Stress
Index (RSI), Mean Productivity (MP), Geometric Mean Productivity (GMP),
Harmonic Mean (HM), Mean Relative Performance (MRP), and Percent Yield
Reduction (PYR), along with a convenience wrapper all_indices() that
returns all indices simultaneously. The function mfvst_from_indices()
integrates these indices into a composite stress score using
direction-aware membership values (0–1 scaling) and also averaging,
facilitating genotype ranking and selection (See Vinu et al., 2025;
<doi:10.1007/s12355-025-01595-1>). The package also implements two novel
composite functions: WMFVST(), which computes the Weighted Mean Membership
Function Value for Stress Tolerance, and WASI(), which computes the
Weighted Average Stress Index, both derived from membership function
values (MFV) and raw stress index values, respectively. Beyond stress
indices, the package provides functions for key physiological traits
relevant to sugarcane and other crops: bmap() computes biomass
accumulation and partitioning between leaf, cane/shoot, and root
fractions. chl() estimates total chlorophyll content from Soil-Plant
Analysis Development (SPAD) and Chlorophyll Content Index (CCI) values
using validated quadratic models particularly for sugarcane (See
Krishnapriya et al., 2020; <doi:10.37580/JSR.2019.2.9.150-163>). ctd()
calculates canopy temperature depression (CTD) from ambient and canopy
temperatures, an important indicator of transpiration efficiency. growth()
computes key growth analysis parameters, including Leaf Area Index (LAI),
Net Assimilation Rate (NAR), and Crop Growth Rate (CGR) across crop growth
stages (See Watson, 1958; <doi:10.1093/oxfordjournals.aob.a083596>).
ranking() provides flexible ranking utilities for genotype performance
with multiple tie-handling and NA-placement options. Through these tools,
the package enables researchers to: (i) quantify crop responses to stress
environments, (ii) partition physiological components of yield, (iii)
integrate multiple indices into composite metrics for genotype evaluation,
and (iv) facilitate informed decision making in breeding pipelines, and
plant physiology experiments. By combining physiology-based traits with
quantitative stress indices, 'PhysioIndexR' supports comprehensive crop
evaluation and helps researchers identify multi-stress-resilient superior
genotypes, thereby contributing to genetic improvement and ensuring
sustainable production of food, fuel, and fibre in the era of limited
resources and climate change.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
