%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SurrogateRsq
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Evaluating the Goodness of Fit using the Surrogate R-Squared

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.54
BuildRequires:    R-CRAN-progress >= 1.2.0
BuildRequires:    R-CRAN-scales >= 1.1.1
BuildRequires:    R-CRAN-DescTools >= 0.99.42
BuildRequires:    R-CRAN-PAsso >= 0.1.10
Requires:         R-CRAN-MASS >= 7.3.54
Requires:         R-CRAN-progress >= 1.2.0
Requires:         R-CRAN-scales >= 1.1.1
Requires:         R-CRAN-DescTools >= 0.99.42
Requires:         R-CRAN-PAsso >= 0.1.10

%description
To assess and compare the models' goodness of fit, R-squared is one of the
most popular measures. For categorical data analysis, however, no
universally adopted R-squared measure can resemble the ordinary least
square (OLS) R-squared for linear models with continuous data. This
package implement the surrogate R-squared measure for categorical data
analysis, which is proposed in the study of Dungang Liu, Xiaorui Zhu,
Brandon Greenwell, and Zewei Lin (2022) <doi:10.1111/bmsp.12289>. It can
generate a point or interval measure of the surrogate R-squared. It can
also provide a ranking measure of the percentage contribution of each
variable to the overall surrogate R-squared. This ranking assessment
allows one to check the importance of each variable in terms of their
explained variance. This package can be jointly used with other existing R
packages for variable selection and model diagnostics in the
model-building process.

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
