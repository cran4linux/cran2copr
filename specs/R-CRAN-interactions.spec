%global __brp_check_rpaths %{nil}
%global packname  interactions
%global packver   1.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Comprehensive, User-Friendly Toolkit for Probing Interactions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jtools >= 2.0.3
BuildRequires:    R-CRAN-rlang >= 0.3.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-jtools >= 2.0.3
Requires:         R-CRAN-rlang >= 0.3.0
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-tibble 

%description
A suite of functions for conducting and interpreting analysis of
statistical interaction in regression models that was formerly part of the
'jtools' package. Functionality includes visualization of two- and
three-way interactions among continuous and/or categorical variables as
well as calculation of "simple slopes" and Johnson-Neyman intervals (see
e.g., Bauer & Curran, 2005 <doi:10.1207/s15327906mbr4003_5>). These
capabilities are implemented for generalized linear models in addition to
the standard linear regression context.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
