%global __brp_check_rpaths %{nil}
%global packname  BBSSL
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Bootstrap Spike-and-Slab LASSO

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-glmnet >= 2.0.16
BuildRequires:    R-CRAN-statmod >= 1.4.30
BuildRequires:    R-CRAN-Matrix >= 1.2.17
BuildRequires:    R-CRAN-rmutil >= 1.1.3
BuildRequires:    R-CRAN-svMisc >= 1.1.0
BuildRequires:    R-CRAN-truncnorm >= 1.0.8
BuildRequires:    R-CRAN-greybox >= 0.5.1
BuildRequires:    R-CRAN-mvnfast >= 0.2.5
BuildRequires:    R-methods 
Requires:         R-CRAN-glmnet >= 2.0.16
Requires:         R-CRAN-statmod >= 1.4.30
Requires:         R-CRAN-Matrix >= 1.2.17
Requires:         R-CRAN-rmutil >= 1.1.3
Requires:         R-CRAN-svMisc >= 1.1.0
Requires:         R-CRAN-truncnorm >= 1.0.8
Requires:         R-CRAN-greybox >= 0.5.1
Requires:         R-CRAN-mvnfast >= 0.2.5
Requires:         R-methods 

%description
Posterior sampling for Spike-and-Slab LASSO prior in linear models from
Nie and Rockova <arXiv:2011.14279>.

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
