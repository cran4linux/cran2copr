%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PortfolioAnalytics
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Portfolio Analysis, Including Numerical Methods for Optimization of Portfolios

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-PerformanceAnalytics >= 1.5.1
BuildRequires:    R-CRAN-xts >= 0.10.1
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-GenSA 
BuildRequires:    R-CRAN-ROI.plugin.symphony 
BuildRequires:    R-CRAN-mco 
BuildRequires:    R-CRAN-pso 
Requires:         R-CRAN-PerformanceAnalytics >= 1.5.1
Requires:         R-CRAN-xts >= 0.10.1
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-foreach 
Requires:         R-methods 
Requires:         R-CRAN-GenSA 
Requires:         R-CRAN-ROI.plugin.symphony 
Requires:         R-CRAN-mco 
Requires:         R-CRAN-pso 

%description
Portfolio optimization and analysis routines and graphics.

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
