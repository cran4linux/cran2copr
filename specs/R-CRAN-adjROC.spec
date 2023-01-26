%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  adjROC
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Computing Sensitivity at a Fix Value of Specificity and Vice Versa as Well as Bootstrap Metrics for ROC Curves

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ROCit 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-yardstick 
Requires:         R-CRAN-ROCit 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-yardstick 

%description
For a binary classification the adjusted sensitivity and specificity are
measured for a given fixed threshold. If the threshold for either
sensitivity or specificity is not given, the crossing point between the
sensitivity and specificity curves are returned. For bootstrap procedures,
mean and CI bootstrap values of sensitivity, specificity, crossing point
between specificity and specificity as well as AUC and AUCPR can be
evaluated.

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
