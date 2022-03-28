%global __brp_check_rpaths %{nil}
%global packname  forsearch
%global packver   2.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Outlier Diagnostics for Some Linear Effects and Linear Mixed Effects Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc >= 4.6.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-tibble >= 3.1.6
BuildRequires:    R-CRAN-nlme >= 3.1.152
BuildRequires:    R-CRAN-Cairo >= 1.5.14
Requires:         R-CRAN-Hmisc >= 4.6.0
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-tibble >= 3.1.6
Requires:         R-CRAN-nlme >= 3.1.152
Requires:         R-CRAN-Cairo >= 1.5.14

%description
Identifies potential data outliers and their impact on estimates and
analyses. Uses the forward search approach of Atkinson and Riani, "Robust
Diagnostic Regression Analysis", (2000,<ISBN: o-387-95017-6>) to prepare
descriptive statistics of a dataset that is to be analyzed by stats::lm(),
stats::glm(), or nlme::lme().  Includes graphics functions to display the
descriptive statistics.

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
