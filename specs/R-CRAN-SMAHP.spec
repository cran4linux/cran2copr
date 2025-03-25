%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SMAHP
%global packver   0.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Survival Mediation Analysis of High-Dimensional Proteogenomic Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-fdrtool 
BuildRequires:    R-CRAN-ncvreg 
BuildRequires:    R-CRAN-penAFT 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-glmnet 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-fdrtool 
Requires:         R-CRAN-ncvreg 
Requires:         R-CRAN-penAFT 
Requires:         R-CRAN-survival 
Requires:         R-stats 
Requires:         R-CRAN-glmnet 

%description
SMAHP (pronounced as SOO-MAP) is a novel multi-omics framework for causal
mediation analysis of high-dimensional proteogenomic data with survival
outcomes. The full methodological details can be found in our recent
preprint by Ahn S et al. (2025) <doi:10.48550/arXiv.2503.08606>.

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
