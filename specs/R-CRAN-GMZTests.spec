%global packname  GMZTests
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Tests

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-base 
BuildRequires:    R-CRAN-DCCA 
BuildRequires:    R-CRAN-PerformanceAnalytics 
BuildRequires:    R-CRAN-nonlinearTseries 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-fgpt 
BuildRequires:    R-CRAN-tseries 
Requires:         R-stats 
Requires:         R-base 
Requires:         R-CRAN-DCCA 
Requires:         R-CRAN-PerformanceAnalytics 
Requires:         R-CRAN-nonlinearTseries 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-fgpt 
Requires:         R-CRAN-tseries 

%description
A collection of functions to perform statistical tests of the following
methods: Detrended Fluctuation Analysis, RHODCCA
coefficient,<doi:10.1103/PhysRevE.84.066118>, DMC coefficient, SILVA-FILHO
et al. (2021) <doi:10.1016/j.physa.2020.125285>, Delta RHODCCA
coefficient, Guedes et al. (2018) <doi:10.1016/j.physa.2018.02.148> and
<doi:10.1016/j.dib.2018.03.080> , Delta DMCA coefficient and Delta DMC
coefficient.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
