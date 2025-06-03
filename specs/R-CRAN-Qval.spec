%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Qval
%global packver   1.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          The Q-Matrix Validation Methods Framework

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-GDINA 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-GDINA 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-Rcpp 
Requires:         R-parallel 
Requires:         R-CRAN-plyr 

%description
Provide a variety of Q-matrix validation methods for the generalized
cognitive diagnosis models, including the method based on the generalized
deterministic input, noisy, and gate model (G-DINA) by de la Torre (2011)
<DOI:10.1007/s11336-011-9207-7> discrimination index (the GDI method) by
de la Torre and Chiu (2016) <DOI:10.1007/s11336-015-9467-8>, the Hull
method by Najera et al. (2021) <DOI:10.1111/bmsp.12228>, the stepwise Wald
test method (the Wald method) by Ma and de la Torre (2020)
<DOI:10.1111/bmsp.12156>, the multiple logistic regression‑based Q‑matrix
validation method (the MLR-B method) by Tu et al. (2022)
<DOI:10.3758/s13428-022-01880-x>, the beta method based on signal
detection theory by Li and Chen (2024) <DOI:10.1111/bmsp.12371> and
Q-matrix validation based on relative fit index by Chen et al. (2013)
<DOI:10.1111/j.1745-3984.2012.00185.x>. Different research methods and
iterative procedures during Q-matrix validating are available
<DOI:10.3758/s13428-024-02547-5>.

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
