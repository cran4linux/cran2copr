%global __brp_check_rpaths %{nil}
%global packname  RegSDC
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Information Preserving Regression-Based Tools for Statistical Disclosure Control

License:          Apache License 2.0 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-SSBtools 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-SSBtools 
Requires:         R-CRAN-MASS 
Requires:         R-methods 

%description
Implementation of the methods described in the paper with the above title:
Langsrud, Ø. (2019) <doi:10.1007/s11222-018-9848-9>. The package can be
used to generate synthetic or hybrid continuous microdata, and the
relationship to the original data can be controlled in several ways. A
function for replacing suppressed tabular cell frequencies with decimal
numbers is included.

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
