%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  KlerRSS
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Intelligent Ranked Set Sampling with 'Excel' Integration and SRS Comparison

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides tools for Ranked Set Sampling (RSS) analysis, data import,
statistical estimation, and comparison with Simple Random Sampling (SRS).
The package offers a complete workflow from 'Excel' and CSV data import
and cleaning to RSS implementation, efficiency evaluation, visualization,
and automated reporting. Intelligent ranking procedures based on
correlation analysis, regression models, and machine learning methods are
included to address imperfect ranking commonly encountered in practical
RSS applications. Monte Carlo simulation tools are provided for evaluating
estimator performance under different sampling scenarios. Ranked Set
Sampling was originally introduced by McIntyre (1952)
<doi:10.2307/3001960> as an efficient alternative to simple random
sampling when ranking information is available at low cost. The package
supports researchers, statisticians, and practitioners working in
agricultural, environmental, biological, and other applied sciences.

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
