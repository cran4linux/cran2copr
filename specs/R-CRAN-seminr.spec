%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  seminr
%global packver   2.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Building and Estimating Structural Equation Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DiagrammeR >= 1.0.6
BuildRequires:    R-CRAN-DiagrammeRsvg >= 0.1
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-webp 
BuildRequires:    R-stats 
Requires:         R-CRAN-DiagrammeR >= 1.0.6
Requires:         R-CRAN-DiagrammeRsvg >= 0.1
Requires:         R-parallel 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-webp 
Requires:         R-stats 

%description
A powerful, easy to use syntax for specifying and estimating complex
Structural Equation Models. Models can be estimated using Partial Least
Squares Path Modeling or Covariance-Based Structural Equation Modeling or
covariance based Confirmatory Factor Analysis (Ray, Danks, and Valdez 2021
<doi:10.2139/ssrn.3900621>).

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
