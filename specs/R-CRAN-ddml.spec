%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ddml
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Double/Debiased Machine Learning

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-AER 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-nnls 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-xgboost 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-AER 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-nnls 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-xgboost 

%description
Estimate common causal parameters using double/debiased machine learning
as proposed by Chernozhukov et al. (2018) <doi:10.1111/ectj.12097>. 'ddml'
simplifies estimation based on (short-)stacking as discussed in Ahrens et
al. (2024) <doi:10.1177/1536867X241233641>, which leverages multiple base
learners to increase robustness to the underlying data generating process.

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
