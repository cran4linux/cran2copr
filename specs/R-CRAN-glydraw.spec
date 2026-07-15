%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  glydraw
%global packver   0.6.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.3
Release:          1%{?dist}%{?buildtag}
Summary:          Draw Beautiful Symbol Nomenclature for Glycans

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 4.0.0
BuildRequires:    R-CRAN-glyrepr >= 0.10.0
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-glyparse 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-fs 
Requires:         R-CRAN-ggplot2 >= 4.0.0
Requires:         R-CRAN-glyrepr >= 0.10.0
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-png 
Requires:         R-CRAN-glyparse 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-fs 

%description
A 'ggplot2'-native plotting engine for drawing reproducible beautiful
Symbol Nomenclature for Glycans (SNFG) glycan cartoons from glycan
structure objects or text notations, with support for batch export,
structural highlighting, and deep appearance customization. It follows the
SNFG specification described at
<https://www.ncbi.nlm.nih.gov/glycans/snfg.html>.

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
