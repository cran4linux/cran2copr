%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cNORM
%global packver   3.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Continuous Norming

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.1
BuildRequires:    R-CRAN-leaps >= 3.1
Requires:         R-CRAN-ggplot2 >= 3.5.1
Requires:         R-CRAN-leaps >= 3.1

%description
A comprehensive toolkit for generating continuous test norms in
psychometrics and biometrics, and analyzing model fit. The package offers
both distribution-free modeling using Taylor polynomials and parametric
modeling using the beta-binomial distribution. Originally developed for
achievement tests, it is applicable to a wide range of mental, physical,
or other test scores dependent on continuous or discrete explanatory
variables. The package provides several advantages: It minimizes
deviations from representativeness in subsamples, interpolates between
discrete levels of explanatory variables, and significantly reduces the
required sample size compared to conventional norming per age group. cNORM
enables graphical and analytical evaluation of model fit, accommodates a
wide range of scales including those with negative and descending values,
and even supports conventional norming. It generates norm tables including
confidence intervals. It also includes methods for addressing
representativeness issues through Iterative Proportional Fitting.

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
