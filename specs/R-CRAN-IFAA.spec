%global __brp_check_rpaths %{nil}
%global packname  IFAA
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Inference for Absolute Abundance in Microbiome Analysis

License:          GNU General Public License version 2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-methods >= 3.3.0
BuildRequires:    R-parallel >= 3.3.0
BuildRequires:    R-CRAN-foreach >= 1.4.3
BuildRequires:    R-CRAN-Matrix >= 1.4.0
BuildRequires:    R-CRAN-future >= 1.12.0
BuildRequires:    R-CRAN-HDCI >= 1.0.2
BuildRequires:    R-CRAN-doParallel >= 1.0.11
BuildRequires:    R-CRAN-mathjaxr >= 1.0.1
BuildRequires:    R-CRAN-expm >= 0.999.3
BuildRequires:    R-CRAN-qlcMatrix >= 0.9.7
BuildRequires:    R-CRAN-rlecuyer >= 0.3.3
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-stats 
Requires:         R-methods >= 3.3.0
Requires:         R-parallel >= 3.3.0
Requires:         R-CRAN-foreach >= 1.4.3
Requires:         R-CRAN-Matrix >= 1.4.0
Requires:         R-CRAN-future >= 1.12.0
Requires:         R-CRAN-HDCI >= 1.0.2
Requires:         R-CRAN-doParallel >= 1.0.11
Requires:         R-CRAN-mathjaxr >= 1.0.1
Requires:         R-CRAN-expm >= 0.999.3
Requires:         R-CRAN-qlcMatrix >= 0.9.7
Requires:         R-CRAN-rlecuyer >= 0.3.3
Requires:         R-CRAN-glmnet 
Requires:         R-stats 

%description
A robust approach to make inference on the association of covariates with
the absolute abundance (AA) of 'microbiome' in an ecosystem. It can be
also directly applied to relative abundance (RA) data to make inference on
AA (even if AA data is not available) because the ratio of two RA is equal
ratio of their AA. This algorithm can estimate and test the associations
of interest while adjusting for potential 'confounders'. The estimates of
this method have easy interpretation like a typical regression analysis.
High-dimensional covariates are handled with regularization and it is
implemented by parallel computing. False discovery rate is automatically
controlled by this approach.

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
