%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pvars
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          VAR Modeling for Heterogeneous Panels

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-svars >= 1.3.4
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-DEoptim 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-steadyICA 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vars 
Requires:         R-CRAN-svars >= 1.3.4
Requires:         R-CRAN-clue 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-DEoptim 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-steadyICA 
Requires:         R-utils 
Requires:         R-CRAN-vars 

%description
Implements (1) panel cointegration rank tests, (2) estimators for panel
vector autoregressive (VAR) models, and (3) identification methods for
panel structural vector autoregressive (SVAR) models as described in the
accompanying vignette. The implemented functions allow to account for
cross-sectional dependence and for structural breaks in the deterministic
terms of the VAR processes. Among the large set of functions, particularly
noteworthy are those that implement (1) the correlation-augmented inverse
normal test on the cointegration rank by Arsova and Oersal (2021,
<doi:10.1016/j.ecosta.2020.05.002>), (2) the two-step estimator for pooled
cointegrating vectors by Breitung (2005, <doi:10.1081/ETC-200067895>), and
(3) the pooled identification based on independent component analysis by
Herwartz and Wang (2024, <doi:10.1002/jae.3044>).

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
