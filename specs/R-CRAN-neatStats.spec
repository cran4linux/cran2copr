%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  neatStats
%global packver   1.13.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.13.5
Release:          1%{?dist}%{?buildtag}
Summary:          Neat and Painless Statistical Reporting

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-fBasics 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-bayestestR 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-MBESS 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-ez 
BuildRequires:    R-CRAN-Exact 
BuildRequires:    R-CRAN-BayesFactor 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-logspline 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-fBasics 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-bayestestR 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-MBESS 
Requires:         R-CRAN-car 
Requires:         R-CRAN-ez 
Requires:         R-CRAN-Exact 
Requires:         R-CRAN-BayesFactor 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-logspline 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-graphics 

%description
User-friendly, clear and simple statistics, primarily for publication in
psychological science. The main functions are wrappers for other packages,
but there are various additions as well. Every relevant step from data
aggregation to reportable printed statistics is covered for basic
experimental designs.

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
