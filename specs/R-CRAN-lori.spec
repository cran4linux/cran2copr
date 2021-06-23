%global __brp_check_rpaths %{nil}
%global packname  lori
%global packver   2.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Imputation of High-Dimensional Count Data using Side Information

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-rARPACK 
BuildRequires:    R-CRAN-svd 
Requires:         R-stats 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-rARPACK 
Requires:         R-CRAN-svd 

%description
Analysis, imputation, and multiple imputation of count data using
covariates. LORI uses a log-linear Poisson model where main row and column
effects, as well as effects of known covariates and interaction terms can
be fitted. The estimation procedure is based on the convex optimization of
the Poisson loss penalized by a Lasso type penalty and a nuclear norm.
LORI returns estimates of main effects, covariate effects and
interactions, as well as an imputed count table. The package also contains
a multiple imputation procedure. The methods are described in Robin,
Josse, Moulines and Sardy (2019) <arXiv:1703.02296v4>.

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
