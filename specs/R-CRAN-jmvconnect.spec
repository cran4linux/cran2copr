%global __brp_check_rpaths %{nil}
%global packname  jmvconnect
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Connect to the 'jamovi' Statistical Spreadsheet

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-jmvcore >= 1.2.19
BuildRequires:    R-CRAN-Rcpp >= 0.12.16
BuildRequires:    R-CRAN-evaluate 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-jmvcore >= 1.2.19
Requires:         R-CRAN-Rcpp >= 0.12.16
Requires:         R-CRAN-evaluate 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-httr 

%description
Methods to access data sets from the 'jamovi' statistical spreadsheet (see
<https://www.jamovi.org> for more information) from R.

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
