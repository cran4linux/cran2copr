%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  carbonate
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Interact with 'carbon.js'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-clipr 
BuildRequires:    R-CRAN-details 
BuildRequires:    R-CRAN-httpuv 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-RSelenium 
BuildRequires:    R-CRAN-rtweet 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-wdman 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-clipr 
Requires:         R-CRAN-details 
Requires:         R-CRAN-httpuv 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-RSelenium 
Requires:         R-CRAN-rtweet 
Requires:         R-utils 
Requires:         R-CRAN-wdman 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-yaml 

%description
Create beautiful images of source code using
'carbon.js'<https://carbon.now.sh/about>.

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
