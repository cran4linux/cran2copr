%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bcfrailphdv
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bivariate Correlated Frailty Models with Varied Variances

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bcfrailph >= 0.1.1
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-stats 
Requires:         R-CRAN-bcfrailph >= 0.1.1
Requires:         R-CRAN-survival 
Requires:         R-stats 

%description
Fit and simulate bivariate correlated frailty models with proportional
hazard structure. Frailty distributions, such as gamma and lognormal
models are supported for semiparametric procedures. Frailty variances of
the two subjects can be varied or equal. Details on the models are
available in book of Wienke (2011,ISBN:978-1-4200-7388-1). Bivariate gamma
fit is obtained using the approach given in Iachine (1995) with
modifications. Lognormal fit is based on the approach by Ripatti and
Palmgren (2000) <doi:10.1111/j.0006-341X.2000.01016.x>. Frailty
distributions, such as gamma, inverse gaussian and power variance frailty
models are supported for parametric approach.

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
