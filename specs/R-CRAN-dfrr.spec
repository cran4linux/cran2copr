%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dfrr
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Dichotomized Functional Response Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fda >= 5.1.4
BuildRequires:    R-CRAN-tmvtnorm >= 1.4
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
Requires:         R-CRAN-fda >= 5.1.4
Requires:         R-CRAN-tmvtnorm >= 1.4
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 

%description
Implementing Function-on-Scalar Regression model in which the response
function is dichotomized and observed sparsely. This package provides
smooth estimations of functional regression coefficients and principal
components for the dichotomized functional response regression (dfrr)
model.

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
