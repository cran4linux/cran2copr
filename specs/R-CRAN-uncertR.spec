%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  uncertR
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Bootstrap Prediction Uncertainty and Its Biological Drivers in Gene-Expression Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-splines 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-future.apply 
Requires:         R-splines 
Requires:         R-stats 
Requires:         R-graphics 

%description
Fits bootstrap ensembles of penalized regression models on bulk
gene-expression data, derives per-sample uncertainty scores from
out-of-bag predictions, and tests whether technical covariates explain
that uncertainty. The bootstrap method is described by Efron and
Tibshirani (1993, ISBN:9780412042317), and elastic-net regression follows
Friedman, Hastie, and Tibshirani (2010) <doi:10.18637/jss.v033.i01>. The
optional immunedeconv package, used for immune-cell deconvolution, is
available from GitHub <https://github.com/omnideconv/immunedeconv>.

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
