%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  countfitteR
%global packver   1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Comprehensive Automatized Evaluation of Distribution Models for Count Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pscl 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-shiny 
Requires:         R-stats 
Requires:         R-CRAN-pscl 
Requires:         R-tools 
Requires:         R-utils 

%description
A large number of measurements generate count data. This is a statistical
data type that only assumes non-negative integer values and is generated
by counting. Typically, counting data can be found in biomedical
applications, such as the analysis of DNA double-strand breaks. The number
of DNA double-strand breaks can be counted in individual cells using
various bioanalytical methods. For diagnostic applications, it is relevant
to record the distribution of the number data in order to determine their
biomedical significance (Roediger, S. et al., 2018. Journal of Laboratory
and Precision Medicine. <doi:10.21037/jlpm.2018.04.10>). The software
offers functions for a comprehensive automated evaluation of distribution
models of count data. In addition to programmatic interaction, a graphical
user interface (web server) is included, which enables fast and
interactive data-scientific analyses. The user is supported in selecting
the most suitable counting distribution for his own data set.

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
