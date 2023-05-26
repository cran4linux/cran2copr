%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CooRTweet
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Coordinated Networks Detection on Social Media

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-tidytable 
BuildRequires:    R-CRAN-RcppSimdJson 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-tidytable 
Requires:         R-CRAN-RcppSimdJson 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-stringi 

%description
Detects a variety of coordinated actions on Twitter and outputs the
network of coordinated users along with related information.

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
