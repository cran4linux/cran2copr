%global __brp_check_rpaths %{nil}
%global packname  mapscanner
%global packver   0.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Print Maps, Draw on Them, Scan Them Back in

License:          GPL-3 | BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-pdftools 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-reproj 
BuildRequires:    R-CRAN-RNiftyReg 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-slippymath 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-pdftools 
Requires:         R-CRAN-png 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-reproj 
Requires:         R-CRAN-RNiftyReg 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-slippymath 
Requires:         R-CRAN-tibble 

%description
Enables preparation of maps to be printed and drawn on. Modified maps can
then be scanned back in, and hand-drawn marks converted to spatial
objects.

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
