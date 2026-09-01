%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rdborrow
%global packver   0.0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          External Control Borrowing for Rare Disease Trials

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-futile.logger 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-CVXR 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-futile.logger 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-CVXR 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-progress 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 

%description
Implements causal inference methods for incorporating external control
data into randomized controlled trials (RCTs) with longitudinal outcomes.
Provides an analysis module supporting weighting-based methods such as
inverse probability weighting (IPW) and augmented inverse probability
weighting (AIPW), difference-in-differences (DID), and synthetic control
approaches for borrowing external control information, as well as a
simulation module for generating trial and external control data,
evaluating estimator performance via Monte Carlo studies, and conducting
power analyses for sample size determination. Methods are based on Zhou et
al. (2024) <doi:10.1093/biostatistics/kxae012> and Zhou et al. (2024)
<doi:10.1080/01621459.2024.2395586>.

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
