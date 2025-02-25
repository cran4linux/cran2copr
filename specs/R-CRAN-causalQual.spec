%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  causalQual
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Causal Inference for Qualitative Outcomes

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-AER 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggsci 
BuildRequires:    R-CRAN-grf 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ocf 
BuildRequires:    R-CRAN-rdrobust 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-AER 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggsci 
Requires:         R-CRAN-grf 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ocf 
Requires:         R-CRAN-rdrobust 
Requires:         R-CRAN-sandwich 
Requires:         R-stats 
Requires:         R-CRAN-stringr 

%description
Implements the framework introduced in Di Francesco and Mellace (2025)
<doi:10.48550/arXiv.2502.11691>, shifting the focus to well-defined and
interpretable estimands that quantify how treatment affects the
probability distribution over outcome categories. It supports
selection-on-observables, instrumental variables, regression
discontinuity, and difference-in-differences designs.

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
