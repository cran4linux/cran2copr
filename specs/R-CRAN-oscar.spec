%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  oscar
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Subset Cardinality Regression (OSCAR) Models Using the L0-Pseudonorm

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-hamlet 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-pROC 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-hamlet 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-utils 
Requires:         R-CRAN-pROC 

%description
Optimal Subset Cardinality Regression (OSCAR) models offer regularized
linear regression using the L0-pseudonorm, conventionally known as the
number of non-zero coefficients. The package estimates an optimal subset
of features using the L0-penalization via cross-validation, bootstrapping
and visual diagnostics. Effective Fortran implementations are offered
along the package for finding optima for the DC-decomposition, which is
used for transforming the discrete L0-regularized optimization problem
into a continuous non-convex optimization task. These optimization modules
include DBDC ('Double Bundle method for nonsmooth DC optimization' as
described in Joki et al. (2018) <doi:10.1137/16M1115733>) and LMBM
('Limited Memory Bundle Method for large-scale nonsmooth optimization' as
in Haarala et al. (2004) <doi:10.1080/10556780410001689225>). The OSCAR
models are comprehensively exemplified in Halkola et al. (2023)
<doi:10.1371/journal.pcbi.1010333>). Multiple regression model families
are supported: Cox, logistic, and Gaussian.

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
