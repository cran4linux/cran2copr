%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mcr
%global packver   1.3.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Method Comparison Regression

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-robslopes 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-robslopes 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 

%description
Regression methods to quantify the relation between two measurement
methods are provided by this package. In particular it addresses
regression problems with errors in both variables and without repeated
measurements. It implements the CLSI recommendations (see J. A. Budd et
al. (2018,
<https://clsi.org/standards/products/method-evaluation/documents/ep09/>)
for analytical method comparison and bias estimation using patient
samples. Furthermore, algorithms for Theil-Sen and equivariant
Passing-Bablok estimators are implemented, see F. Dufey (2020,
<doi:10.1515/ijb-2019-0157>) and J. Raymaekers and F. Dufey (2022,
<arXiv:2202:08060>). A comprehensive overview over the implemented methods
and references can be found in the manual pages "mcr-package" and "mcreg".

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
