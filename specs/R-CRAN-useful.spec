%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  useful
%global packver   1.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.7
Release:          1%{?dist}%{?buildtag}
Summary:          A Collection of Handy, Useful Functions

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-purrr >= 0.1.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-purrr >= 0.1.0
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plyr 
Requires:         R-stats 
Requires:         R-CRAN-scales 
Requires:         R-utils 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rlang 

%description
A set of little functions that have been found useful to do little odds
and ends such as plotting the results of K-means clustering, substituting
special text characters, viewing parts of a data.frame, constructing
formulas from text and building design and response matrices.

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
