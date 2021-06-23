%global __brp_check_rpaths %{nil}
%global packname  PO.EN
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          An Elastic-Net Regularized Presence-Only Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-PUlasso 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-PUlasso 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-pROC 

%description
Presence-only model with Elastic Net penalty is a regularized generalized
linear model training on the presence-absence response. This package
provides functions for tuning and fitting the presence-only model. The
presence-only model can be used to predict regulatory effects of genetic
variants at sequence-level resolution by integrating a large number of
epigenetic features and massively parallel reporter assays (MPRAs).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
