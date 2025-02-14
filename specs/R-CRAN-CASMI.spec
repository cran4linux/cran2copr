%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CASMI
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          'CASMI'-Based Functions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-EntropyEstimation 
BuildRequires:    R-CRAN-entropy 
BuildRequires:    R-stats 
Requires:         R-CRAN-EntropyEstimation 
Requires:         R-CRAN-entropy 
Requires:         R-stats 

%description
Contains Coverage Adjusted Standardized Mutual Information ('CASMI')-based
functions. 'CASMI' is a fundamental concept of a series of methods. For
more information about 'CASMI' and 'CASMI'-related methods, please refer
to the corresponding publications (e.g., a feature selection method, Shi,
J., Zhang, J., & Ge, Y. (2019) <doi:10.3390/e21121179>, and a dataset
quality measurement method, Shi, J., Zhang, J., & Ge, Y. (2019)
<doi:10.1109/ICHI.2019.8904553>) or contact the package author for the
latest updates.

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
