%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  smarter
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Collection of Modified R Functions to Make Basic Coding More Convenient

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-gplots 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-rmarkdown 

%description
A collection of recycled and modified R functions to aid in file
manipulation, data exploration, wrangling, optimization, and object
manipulation. Other functions aid in convenient data visualization, loop
progression, software packaging, and installation.

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
