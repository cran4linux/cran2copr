%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pkgstats
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Metrics of R Packages

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ami 
BuildRequires:    R-CRAN-brio 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-roxygen2 
BuildRequires:    R-CRAN-sys 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-cpp11 
Requires:         R-CRAN-ami 
Requires:         R-CRAN-brio 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-memoise 
Requires:         R-methods 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-roxygen2 
Requires:         R-CRAN-sys 
Requires:         R-CRAN-withr 

%description
Static code analyses for R packages using the external code-tagging
libraries 'ctags' and 'gtags'. Static analyses enable packages to be
analysed very quickly, generally a couple of seconds at most. The package
also provides access to a database generating by applying the main
function to the full 'CRAN' archive, enabling the statistical properties
of any package to be compared with all other 'CRAN' packages.

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
