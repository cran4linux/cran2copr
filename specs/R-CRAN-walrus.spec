%global __brp_check_rpaths %{nil}
%global packname  walrus
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Statistical Methods

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jmvcore >= 2.2
BuildRequires:    R-CRAN-WRS2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-jmvcore >= 2.2
Requires:         R-CRAN-WRS2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-R6 

%description
A toolbox of common robust statistical tests, including robust
descriptives, robust t-tests, and robust ANOVA. It is also available as a
module for 'jamovi' (see <https://www.jamovi.org> for more information).
Walrus is based on the WRS2 package by Patrick Mair, which is in turn
based on the scripts and work of Rand Wilcox. These analyses are described
in depth in the book 'Introduction to Robust Estimation & Hypothesis
Testing'.

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
