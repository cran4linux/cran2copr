%global packname  sureLDA
%global packver   0.1.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Novel Multi-Disease Automated Phenotyping Method for the EHR

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-MAP 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-MAP 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 

%description
A statistical learning method to simultaneously predict a range of target
phenotypes using codified and natural language processing (NLP)-derived
Electronic Health Record (EHR) data. See Ahuja et al (2020) JAMIA
<doi:10.1093/jamia/ocaa079> for details.

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
