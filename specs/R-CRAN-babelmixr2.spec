%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  babelmixr2
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Use 'nlmixr2' to Interact with Open Source and Commercial Software

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-nlmixr2 >= 2.0.8
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-lotri 
BuildRequires:    R-CRAN-nlmixr2est 
BuildRequires:    R-CRAN-nonmem2rx 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-qs 
BuildRequires:    R-CRAN-rex 
BuildRequires:    R-CRAN-rxode2 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-rxode2parse 
Requires:         R-CRAN-nlmixr2 >= 2.0.8
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-lotri 
Requires:         R-CRAN-nlmixr2est 
Requires:         R-CRAN-nonmem2rx 
Requires:         R-methods 
Requires:         R-CRAN-qs 
Requires:         R-CRAN-rex 
Requires:         R-CRAN-rxode2 

%description
Run other estimation and simulation software via the 'nlmixr2' (Fidler et
al (2019) <doi:10.1002/psp4.12445>) interface including 'PKNCA', 'NONMEM'
and 'Monolix'. While not required, you can get/install the
'lixoftConnectors' package in the 'Monolix' installation, as described at
the following url
<https://monolix.lixoft.com/monolix-api/lixoftconnectors_installation/>.
When 'lixoftConnectors' is available, 'Monolix' can be run directly
instead of setting up command line usage.

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
