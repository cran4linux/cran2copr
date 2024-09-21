%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HDclust
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Clustering High Dimensional Data with Hidden Markov Model on Variable Blocks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.16
BuildRequires:    R-CRAN-Rtsne >= 0.11
BuildRequires:    R-CRAN-RcppProgress >= 0.1
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 0.12.16
Requires:         R-CRAN-Rtsne >= 0.11
Requires:         R-CRAN-RcppProgress >= 0.1
Requires:         R-methods 

%description
Clustering of high dimensional data with Hidden Markov Model on Variable
Blocks (HMM-VB) fitted via Baum-Welch algorithm. Clustering is performed
by the Modal Baum-Welch algorithm (MBW), which finds modes of the density
function. Lin Lin and Jia Li (2017)
<https://jmlr.org/papers/v18/16-342.html>.

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
