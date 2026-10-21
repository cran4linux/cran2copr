%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  regsensitivity
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Regression Sensitivity Analysis for Omitted Variable Bias

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-nloptr >= 2.0.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-stats 
BuildRequires:    R-grid 
BuildRequires:    R-parallel 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-nloptr >= 2.0.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-stats 
Requires:         R-grid 
Requires:         R-parallel 

%description
Sensitivity analysis for linear regression coefficients in the presence of
omitted variables. Implements the identified-set and breakdown-point
analyses of Diegert, Masten and Poirier (2026)
<doi:10.48550/arXiv.2206.02303>, Oster (2019)
<doi:10.1080/07350015.2016.1227711> and Masten and Poirier (2026)
<doi:10.1257/aer.20230242>. Provides bounds on regression coefficients
under relaxations of the no-omitted-variables assumption indexed by
interpretable sensitivity parameters, the breakdown point of a hypothesis
about the long-regression coefficient, and plotting helpers.

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
