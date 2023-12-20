%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  plumbertableau
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Turn 'Plumber' APIs into 'Tableau' Extensions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plumber >= 1.1.0
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-httpuv 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-later 
BuildRequires:    R-CRAN-promises 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-debugme 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-urltools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-plumber >= 1.1.0
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-httpuv 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-later 
Requires:         R-CRAN-promises 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-debugme 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-urltools 
Requires:         R-utils 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-knitr 

%description
Build 'Plumber' APIs that can be used in 'Tableau' workbooks. Annotations
in R comments allow APIs to conform to the 'Tableau Analytics Extension'
specification, so that R code can be used to power 'Tableau' workbooks.

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
