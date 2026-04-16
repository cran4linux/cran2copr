%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nmfkc
%global packver   0.6.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.7
Release:          1%{?dist}%{?buildtag}
Summary:          Non-Negative Matrix Factorization with Kernel Covariates

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-grDevices 

%description
Performs Non-negative Matrix Factorization (NMF) with Kernel Covariates.
Given an observation matrix and kernel covariates, it optimizes both a
basis matrix and a parameter matrix. Notably, if the kernel matrix is an
identity matrix, the method simplifies to standard NMF. Also provides NMF
with Random Effects (NMF-RE) via nmfre(), which estimates a mixed-effects
model combining covariate-driven scores with unit-specific random effects
together with wild bootstrap inference, and NMF-based Structural Equation
Modeling (NMF-SEM) via nmf.sem(), which fits a two-block input-output
model for blind source separation and path analysis. References: Satoh
(2025) <doi:10.48550/arXiv.2403.05359>; Satoh (2025)
<doi:10.48550/arXiv.2510.10375>; Satoh (2025)
<doi:10.48550/arXiv.2512.18250>; Satoh (2026)
<doi:10.48550/arXiv.2603.01468>; Satoh (2026)
<doi:10.1007/s42081-025-00314-0>.

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
