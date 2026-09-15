%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  featR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Unified Toolkit for Feature Selection

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-data.table 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-withr 

%description
Filter, wrapper, and embedded feature-selection methods behind a
consistent set of functions that share one calling convention and one
return type: correlation and chi-squared filters, information gain, LASSO
and elastic net, Bayesian model comparison, Boruta, recursive feature
elimination, random forest importance, multivariate adaptive regression
splines, support vector machine recursive feature elimination, stepwise
selection, and principal component / singular value decomposition helpers.
The implemented methods follow Tibshirani (1996)
<doi:10.1111/j.2517-6161.1996.tb02080.x>, Zou and Hastie (2005)
<doi:10.1111/j.1467-9868.2005.00503.x>, Friedman (1991)
<doi:10.1214/aos/1176347963>, Breiman (2001)
<doi:10.1023/A:1010933404324>, Guyon, Weston, Barnhill and Vapnik (2002)
<doi:10.1023/A:1012487302797>, Kursa and Rudnicki (2010)
<doi:10.18637/jss.v036.i11>, and Vehtari, Gelman and Gabry (2017)
<doi:10.1007/s11222-016-9696-4>. Heavy modeling engines are optional and
only required by the functions that use them.

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
