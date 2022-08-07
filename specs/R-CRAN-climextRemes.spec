%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  climextRemes
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Analyzing Climate Extremes

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-extRemes >= 2.0.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-boot 
Requires:         R-CRAN-extRemes >= 2.0.0
Requires:         R-methods 
Requires:         R-CRAN-boot 

%description
Functions for fitting GEV and POT (via point process fitting) models for
extremes in climate data, providing return values, return probabilities,
and return periods for stationary and nonstationary models. Also provides
differences in return values and differences in log return probabilities
for contrasts of covariate values. Functions for estimating risk ratios
for event attribution analyses, including uncertainty. Under the hood,
many of the functions use functions from 'extRemes', including for fitting
the statistical models. Details are given in Paciorek, Stone, and Wehner
(2018) <doi:10.1016/j.wace.2018.01.002>.

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
