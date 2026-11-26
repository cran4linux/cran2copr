%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pharos
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Descriptive Statistics Graphics and Utilities

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.6.0
Requires:         R-core >= 4.6.0
BuildRequires:    R-CRAN-bedrock >= 0.1.18
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-grid 
Requires:         R-CRAN-bedrock >= 0.1.18
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-stringi 
Requires:         R-methods 
Requires:         R-CRAN-base64enc 
Requires:         R-grid 

%description
Draws the statistical graphics of the 'DescToolsX' ecosystem on top of
base graphics: distribution and density displays, bivariate and
categorical plots, diagnostic and model evaluation panels, and a faceting
mechanism for arranging them. A theme system resolves colours, symbols and
layout centrally, so a consistent look can be set once rather than
repeated at every call. The package also contains the colour conversion
and palette tools, the geometry helpers, the number and string formatting
routines and the HTML output utilities that the plots are built from. It
is self contained and usable without the rest of the suite.

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
