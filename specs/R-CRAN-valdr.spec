%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  valdr
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Access and Analyse 'VALD' Data via Our External 'APIs'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-keyring 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-keyring 
Requires:         R-CRAN-jsonlite 

%description
Provides helper functions and wrappers to simplify authentication, data
retrieval, and result processing from the 'VALD' 'APIs'. Designed to
streamline integration for analysts and researchers working with 'VALD's
external 'APIs'. For further documentation on integrating with 'VALD'
'APIs', see:
<https://support.vald.com/hc/en-au/articles/23415335574553-How-to-integrate-with-VALD-APIs>.
For a step-by-step guide to using this package, see:
<https://support.vald.com/hc/en-au/articles/48730811824281-A-guide-to-using-the-valdr-R-package>.

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
