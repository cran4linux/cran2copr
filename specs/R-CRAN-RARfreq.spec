%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RARfreq
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Response Adaptive Randomization with 'Frequentist' Approach

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-latex2exp 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-latex2exp 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-patchwork 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-reshape2 

%description
Provides functions and command-line user interface to generate allocation
sequence by response-adaptive randomization for clinical trials. The
package currently supports two response-adaptive randomization procedures,
Doubly Adaptive Biased Coin Design ('DBCD') and Sequential
Estimation-adjusted Urn Model ('SEU'), for two endpoints, binary and
normal. One-sided proportion (or mean) difference and Chi-square (or
'ANOVA') hypothesis testing methods are also available in the package to
facilitate the inference for treatment effect under different sample sizes
and the inference for sample size under different treatment effects.
Additionally, the package provides comprehensive and efficient tools to
allow one to evaluate and compare the performance of randomization
procedures and tests based on various criteria. Five allocation functions
for 'DBCD' and six addition rule functions for 'SEU' are implemented to
target allocations such as 'Neyman', 'Rosenberger' and 'Urn' allocations.

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
