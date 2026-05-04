%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  savvyGLM
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Linear Models with Slab and Shrinkage Estimators

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-glm2 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-CVXR 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-expm 
Requires:         R-parallel 
Requires:         R-CRAN-glm2 
Requires:         R-utils 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-CVXR 

%description
Provides a flexible framework for fitting generalized linear models (GLMs)
with slab and shrinkage estimators. Methods include the Stein estimator
(St), Diagonal Shrinkage (DSh), Simple Slab Regression (SR), Generalized
Slab Regression (GSR), Ledoit-Wolf Linear Shrinkage (LW),
Quadratic-Inverse Shrinkage (QIS), and Shrinkage (Sh), all integrated into
the iteratively reweighted least squares (IRLS) algorithm. This approach
enhances estimation accuracy, convergence, and robustness in the presence
of multicollinearity. The best-fitting model is selected based on the
Akaike Information Criterion (AIC). Methods are related to methods
described in Marschner (2011) <doi:10.32614/RJ-2011-012>, Asimit et al.
(2025) <https://openaccess.city.ac.uk/id/eprint/35005/>, Ledoit and Wolf
(2004) <doi:10.1016/S0047-259X(03)00096-4>, and Ledoit and Wolf (2022)
<doi:10.3150/20-BEJ1315>.

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
