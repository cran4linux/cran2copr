%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ddst
%global packver   1.6.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.11
Release:          1%{?dist}%{?buildtag}
Summary:          Data Driven Smooth Tests

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.7
Requires:         R-core >= 2.7
BuildArch:        noarch
BuildRequires:    R-CRAN-polynom 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-orthopolynom 
BuildRequires:    R-CRAN-evd 
Requires:         R-CRAN-polynom 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-orthopolynom 
Requires:         R-CRAN-evd 

%description
Smooth tests are data driven (alternative hypothesis is dynamically
selected based on data). In this package you will find two groups of
smooth of test: goodness-of-fit tests and nonparametric tests for
comparing distributions. Among goodness-of-fit tests there are tests for
exponent, Gaussian, Gumbel and uniform distribution. Among nonparametric
tests there are tests for stochastic dominance, k-sample test, test with
umbrella alternatives and test for change-point problems.

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
