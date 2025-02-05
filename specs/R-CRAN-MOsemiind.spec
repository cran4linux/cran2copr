%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MOsemiind
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Marshall-Olkin Shock Models with Semi-Independent Time

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-stats 
Requires:         R-CRAN-copula 
Requires:         R-graphics 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-shiny 
Requires:         R-stats 

%description
Provides tools for analyzing Marshall-Olkin shock models semi-independent
time. It includes interactive 'shiny' applications for exploring
copula-based dependence structures, along with functions for modeling and
visualization. The methods are based on Mijanovic and Popovic (2024,
submitted) "An R package for Marshall-Olkin shock models with
semi-independent times."

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
