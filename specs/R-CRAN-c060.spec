%global __brp_check_rpaths %{nil}
%global packname  c060
%global packver   0.2-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.8
Release:          1%{?dist}%{?buildtag}
Summary:          Extended Inference for Lasso and Elastic-Net Regularized Cox and Generalized Linear Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-mlegp 
BuildRequires:    R-CRAN-tgp 
BuildRequires:    R-CRAN-peperr 
BuildRequires:    R-CRAN-penalizedSVM 
BuildRequires:    R-CRAN-lattice 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-survival 
Requires:         R-parallel 
Requires:         R-CRAN-mlegp 
Requires:         R-CRAN-tgp 
Requires:         R-CRAN-peperr 
Requires:         R-CRAN-penalizedSVM 
Requires:         R-CRAN-lattice 

%description
The c060 package provides additional functions to perform stability
selection, model validation and parameter tuning for glmnet models.

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
