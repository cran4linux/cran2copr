%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hmer
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          History Matching and Emulation Package

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-isoband 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-pdist 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-isoband 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-pdist 

%description
A set of objects and functions for Bayes Linear emulation and history
matching. Core functionality includes automated training of emulators to
data, diagnostic functions to ensure suitability, and a variety of
proposal methods for generating 'waves' of points. For details on the
mathematical background, there are many papers available on the topic (see
references attached to function help files); for details of the functions
in this package, consult the manual or help files.

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
