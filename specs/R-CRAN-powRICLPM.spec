%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  powRICLPM
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Perform Power Analysis for the RI-CLPM and STARTS Model

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan >= 0.6.7
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-future 
Requires:         R-CRAN-lavaan >= 0.6.7
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-future 

%description
Perform user-friendly power analyses for the random intercept cross-lagged
panel model (RI-CLPM) and the bivariate stable trait autoregressive trait
state (STARTS) model. The strategy as proposed by Mulder (2023)
<doi:10.1080/10705511.2022.2122467> is implemented. Extensions include the
use of parameter constraints over time, bounded estimation, generation of
data with skewness and kurtosis, and the option to setup the power
analysis for Mplus.

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
