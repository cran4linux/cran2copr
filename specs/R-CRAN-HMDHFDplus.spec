%global __brp_check_rpaths %{nil}
%global packname  HMDHFDplus
%global packver   1.9.17
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.17
Release:          1%{?dist}%{?buildtag}
Summary:          Read Human Mortality Database and Human Fertility Database Data from the Web

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-rvest 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-rvest 

%description
Utilities for reading data from the Human Mortality Database
(<https://www.mortality.org>), Human Fertility Database
(<https://www.humanfertility.org>), and similar databases from the web or
locally into an R session as data.frame objects. These are the two most
widely used sources of demographic data to study basic demographic change,
trends, and develop new demographic methods. Other supported databases at
this time include the Human Fertility Collection
(<https://www.fertilitydata.org>), The Japanese Mortality Database
(<https://www.ipss.go.jp/p-toukei/JMD/index-en.html>), and the Canadian
Human Mortality Database (<http://www.bdlc.umontreal.ca/chmd/>). Arguments
and data are standardized.

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
