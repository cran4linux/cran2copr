%global __brp_check_rpaths %{nil}
%global packname  msaeRB
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Ratio Benchmarking for Multivariate Small Area Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
Requires:         R-CRAN-magic 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-MASS 
Requires:         R-stats 

%description
Implements multivariate ratio benchmarking small area estimation. This
package provides ratio benchmarking estimation for univariate and
multivariate small area estimation and its MSE. In fact, MSE estimators
for ratio benchmark are not readily available, so resampling method that
called parametric bootstrap is applied. The ratio benchmark model and
parametric bootstrap in this package are based on the model proposed in
small area estimation. J.N.K Rao and Isabel Molina (2015, ISBN:
978-1-118-73578-7).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
