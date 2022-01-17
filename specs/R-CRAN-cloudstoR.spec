%global __brp_check_rpaths %{nil}
%global packname  cloudstoR
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simplifies Access to Cloudstor API

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-getPass 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-keyring 
BuildRequires:    R-CRAN-rio 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-XML 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-getPass 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-keyring 
Requires:         R-CRAN-rio 
Requires:         R-utils 
Requires:         R-CRAN-XML 

%description
Access Cloudstor via their WebDAV API. This package can read, write, and
navigate Cloudstor from R.

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
