%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CERFIT
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Causal Effect Random Forest of Interaction Trees

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-CRAN-CBPS 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-twang 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-partykit 
Requires:         R-CRAN-CBPS 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-twang 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-CRAN-glmnet 

%description
Fits a Causal Effect Random Forest of Interaction Tress (CERFIT) which is
a modification of the Random Forest algorithm where each split is chosen
to maximize subgroup treatment heterogeneity. Doing this allows it to
estimate the individualized treatment effect for each observation in
either randomized controlled trial (RCT) or observational data. For more
information see L. Li, R. A. Levine, and J. Fan (2022)
<doi:10.1002/sta4.457>.

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
