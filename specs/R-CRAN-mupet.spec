%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mupet
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multiclass Performance Evaluation Toolkit

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-yardstick 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-yardstick 

%description
Implementation of custom 'tidymodels' metrics for multi-class prediction
models with a single negative class. Currently are implemented
macro-average sensitivity and specificity as in Mortaz, Ebrahim (2020)
"Imbalance accuracy metric for model selection in multi-class imbalance
classification problems” <doi:10.1016/j.knosys.2020.106490> and a
generalized weighted Youden index as in Li, D.L., Shen F., Yin Y., Peng
J.X and Chen P.Y. (2013) “Weighted Youden index and its
two-independent-sample comparison based on weighted sensitivity and
specificity” <doi:10.3760/cma.j.issn.0366-6999.20123102>.

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
