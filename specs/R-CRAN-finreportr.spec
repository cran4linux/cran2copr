%global __brp_check_rpaths %{nil}
%global packname  finreportr
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Financial Data from U.S. Securities and Exchange Commission

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-XBRL 
BuildRequires:    R-CRAN-curl 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-XBRL 
Requires:         R-CRAN-curl 

%description
Download and display company financial data from the U.S. Securities and
Exchange Commission's EDGAR database. It contains a suite of functions
with web scraping and XBRL parsing capabilities that allows users to
extract data from EDGAR in an automated and scalable manner. See
<https://www.sec.gov/edgar/searchedgar/companysearch.html> for more
information.

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
