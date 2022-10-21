%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RfEmpImp
%global packver   2.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Multiple Imputation using Chained Random Forests

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mice >= 3.9.0
BuildRequires:    R-CRAN-ranger >= 0.12.1
Requires:         R-CRAN-mice >= 3.9.0
Requires:         R-CRAN-ranger >= 0.12.1

%description
An R package for multiple imputation using chained random forests.
Implemented methods can handle missing data in mixed types of variables by
using prediction-based or node-based conditional distributions constructed
using random forests. For prediction-based imputation, the method based on
the empirical distribution of out-of-bag prediction errors of random
forests and the method based on normality assumption for prediction errors
of random forests are provided for imputing continuous variables. And the
method based on predicted probabilities is provided for imputing
categorical variables. For node-based imputation, the method based on the
conditional distribution formed by the predicting nodes of random forests,
and the method based on proximity measures of random forests are provided.
More details of the statistical methods can be found in Hong et al. (2020)
<arXiv:2004.14823>.

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
