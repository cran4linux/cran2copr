%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MaxMC
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Maximized Monte Carlo

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-GenSA 
BuildRequires:    R-CRAN-pso 
BuildRequires:    R-CRAN-GA 
BuildRequires:    R-CRAN-NMOF 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-CRAN-GenSA 
Requires:         R-CRAN-pso 
Requires:         R-CRAN-GA 
Requires:         R-CRAN-NMOF 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 

%description
An implementation of the Monte Carlo techniques described in details by
Dufour (2006) <doi:10.1016/j.jeconom.2005.06.007> and Dufour and Khalaf
(2007) <doi:10.1002/9780470996249.ch24>. The two main features available
are the Monte Carlo method with tie-breaker, mc(), for discrete
statistics, and the Maximized Monte Carlo, mmc(), for statistics with
nuisance parameters.

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
