%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MUGS
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multisource Graph Synthesis with EHR Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-fastDummies 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-grplasso 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-grpreg 
BuildRequires:    R-CRAN-inline 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-rsvd 
BuildRequires:    R-methods 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-fastDummies 
Requires:         R-CRAN-doSNOW 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-grplasso 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-grpreg 
Requires:         R-CRAN-inline 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-pROC 
Requires:         R-parallel 
Requires:         R-CRAN-RcppArmadillo 
Requires:         R-CRAN-rsvd 
Requires:         R-methods 

%description
We develop Multi-source Graph Synthesis (MUGS), an algorithm designed to
create embeddings for pediatric Electronic Health Record (EHR) codes by
leveraging graphical information from three distinct sources: (1)
pediatric EHR data, (2) EHR data from the general patient population, and
(3) existing hierarchical medical ontology knowledge shared across
different patient populations. See Li et al. (2024)
<doi:10.1038/s41746-024-01320-4> for details.

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
