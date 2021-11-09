%global __brp_check_rpaths %{nil}
%global packname  hierbase
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Enabling Hierarchical Multiple Testing

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-hdi 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-SIHR 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-hdi 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-CRAN-SIHR 

%description
Implementation of hierarchical inference based on Meinshausen (2008).
Hierarchical testing of variable importance. Biometrika, 95(2), 265-278
and Renaux, Buzdugan, Kalisch, and Bühlmann, (2020). Hierarchical
inference for genome-wide association studies: a view on methodology with
software. Computational Statistics, 35(1), 1-40. The R-package 'hierbase'
offers tools to perform hierarchical inference for one or multiple data
sets based on ready-to-use (group) test functions or alternatively a user
specified (group) test function. The procedure is based on a hierarchical
multiple testing correction and controls the family-wise error rate
(FWER). The functions can easily be run in parallel. Hierarchical
inference can be applied to (low- or) high-dimensional data sets to find
significant groups or single variables (depending on the signal strength
and correlation structure) in a data-driven and automated procedure.
Possible applications can for example be found in statistical genetics and
statistical genomics.

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
