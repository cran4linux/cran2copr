%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HDANOVA
%global packver   0.8.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.3
Release:          1%{?dist}%{?buildtag}
Summary:          High-Dimensional Analysis of Variance

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mixlm >= 1.4.2
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-RSpectra 
Requires:         R-CRAN-mixlm >= 1.4.2
Requires:         R-CRAN-car 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-RSpectra 

%description
Functions and datasets to support Smilde, Marini, Westerhuis and Liland
(2025, ISBN: 978-1-394-21121-0) "Analysis of Variance for High-Dimensional
Data - Applications in Life, Food and Chemical Sciences". This implements
and imports a collection of methods for HD-ANOVA data analysis with common
interfaces, result- and plotting functions, multiple real data sets and
four vignettes covering a range different applications.

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
