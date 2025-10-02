%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  descsuppR
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Support Functions for (Reproducible) Descriptive Statistics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-descutils 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-nparcomp 
BuildRequires:    R-CRAN-rankFD 
BuildRequires:    R-CRAN-circular 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-descutils 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-nparcomp 
Requires:         R-CRAN-rankFD 
Requires:         R-CRAN-circular 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-purrr 

%description
Contains functions to help with generating tables with descriptive
statistics. In addition, the package can display results of statistical
tests for group comparisons. A wide range of test procedures is supported,
and user-defined test functions can be incorporated.

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
