%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AmoudSurv
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tractable Parametric Odds-Based Regression Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-AHSurv 
BuildRequires:    R-CRAN-flexsurv 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-stats 
BuildRequires:    R-stats4 
Requires:         R-CRAN-AHSurv 
Requires:         R-CRAN-flexsurv 
Requires:         R-CRAN-pracma 
Requires:         R-stats 
Requires:         R-stats4 

%description
Fits tractable fully parametric odds-based regression models for survival
data, including proportional odds (PO), accelerated failure time (AFT),
accelerated odds (AO), and General Odds (GO) models in overall survival
frameworks. Given at least an R function specifying the survivor, hazard
rate and cumulative distribution functions, any user-defined parametric
distribution can be fitted. We applied and evaluated a minimum of
seventeen (17) various baseline distributions that can handle different
failure rate shapes for each of the four different proposed odds-based
regression models. For more information see Bennet et al., (1983)
<doi:10.1002/sim.4780020223>, and Muse et al., (2022)
<doi:10.1016/j.aej.2022.01.033>.

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
