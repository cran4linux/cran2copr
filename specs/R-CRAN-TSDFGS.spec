%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TSDFGS
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Training Set Determination for Genomic Selection

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 

%description
Finds a training set for genomic selection and the size it needs. The
r-score of Ou and Liao (2019) <doi:10.1007/s00122-019-03387-0> is derived
from Pearson's correlation between the genomic estimated breeding values
and the phenotypic values of the test set. optTrain() searches for a good
training set, and SSDFGS() searches for its size. Eighteen criteria are
available to score or optimize a training set, among them A-, D-, E- and
G-optimality, PEVmax, MSPE, CDmean, CDmax, and genomic relationship
criteria (Chen et al. (2024) <doi:10.1007/s00122-024-04766-y>;
Fernandez-Gonzalez et al. (2023) <doi:10.1007/s00122-023-04265-6>). The
computation uses 'Rcpp' and 'RcppEigen', and independent searches can run
on several threads with 'OpenMP'.

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
