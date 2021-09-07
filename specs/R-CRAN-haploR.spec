%global __brp_check_rpaths %{nil}
%global packname  haploR
%global packver   4.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Query 'HaploReg', 'RegulomeDB'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-RUnit 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-RJSONIO 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-RUnit 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-RJSONIO 

%description
A set of utilities for querying 'HaploReg'
<https://pubs.broadinstitute.org/mammals/haploreg/haploreg.php>,
'RegulomeDB' <https://www.regulomedb.org/regulome-search/> web-based
tools. The package connects to 'HaploReg', 'RegulomeDB' searches and
downloads results, without opening web pages, directly from R environment.
Results are stored in a data frame that can be directly used in various
kinds of downstream analyses.

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
