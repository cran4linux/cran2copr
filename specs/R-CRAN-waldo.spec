%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  waldo
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Find Differences Between R Objects

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-diffobj >= 0.3.4
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-fansi 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rematch2 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-diffobj >= 0.3.4
Requires:         R-CRAN-cli 
Requires:         R-CRAN-fansi 
Requires:         R-CRAN-glue 
Requires:         R-methods 
Requires:         R-CRAN-rematch2 
Requires:         R-CRAN-tibble 

%description
Compare complex R objects and reveal the key differences. Designed
particularly for use in testing packages where being able to quickly
isolate key differences makes understanding test failures much easier.

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
