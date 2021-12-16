%global __brp_check_rpaths %{nil}
%global packname  MulvariateRandomForestVarImp
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Variable Importance Measures for Multivariate Random Forests

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.0
BuildRequires:    R-CRAN-MultivariateRandomForest >= 1.1.5
Requires:         R-CRAN-MASS >= 7.3.0
Requires:         R-CRAN-MultivariateRandomForest >= 1.1.5

%description
Calculates two sets of post-hoc variable importance measures for
multivariate random forests. The first set of variable importance measures
are given by the sum of mean split improvements for splits defined by
feature j measured on user-defined examples (i.e., training or testing
samples). The second set of importance measures are calculated on a
per-outcome variable basis as the sum of mean absolute difference of node
values for each split defined by feature j measured on user-defined
examples (i.e., training or testing samples). The user can optionally
threshold both sets of importance measures to include only splits that are
statistically significant as measured using an F-test.

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
