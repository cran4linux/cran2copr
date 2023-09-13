%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  redcapAPI
%global packver   2.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.8.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to 'REDCap'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-chron 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-labelVector 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-keyring 
BuildRequires:    R-CRAN-getPass 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-chron 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-labelVector 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-keyring 
Requires:         R-CRAN-getPass 
Requires:         R-CRAN-yaml 

%description
Access data stored in 'REDCap' databases using the Application Programming
Interface (API).  'REDCap' (Research Electronic Data CAPture;
<https://projectredcap.org>, Harris, et al. (2009)
<doi:10.1016/j.jbi.2008.08.010>, Harris, et al. (2019)
<doi:10.1016/j.jbi.2019.103208>) is a web application for building and
managing online surveys and databases developed at Vanderbilt University.
The API allows users to access data and project meta data (such as the
data dictionary) from the web programmatically. The 'redcapAPI' package
facilitates the process of accessing data with options to prepare an
analysis-ready data set consistent with the definitions in a database's
data dictionary.

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
