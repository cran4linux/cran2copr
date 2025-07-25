%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ICSClust
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tandem Clustering with Invariant Coordinate Selection

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ICS >= 1.4.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-fpc 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-heplots 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-otrimle 
BuildRequires:    R-CRAN-RcppRoll 
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-tclust 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ICS >= 1.4.0
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-fpc 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-heplots 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-otrimle 
Requires:         R-CRAN-RcppRoll 
Requires:         R-CRAN-rrcov 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-tclust 

%description
Implementation of tandem clustering with invariant coordinate selection
with different scatter matrices and several choices for the selection of
components as described in Alfons, A., Archimbaud, A., Nordhausen, K.and
Ruiz-Gazen, A. (2024) <doi:10.1016/j.ecosta.2024.03.002>.

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
