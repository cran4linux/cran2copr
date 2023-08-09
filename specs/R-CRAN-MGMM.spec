%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MGMM
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Missingness Aware Gaussian Mixture Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-CRAN-cluster 
Requires:         R-methods 
Requires:         R-CRAN-mvnfast 
Requires:         R-CRAN-plyr 
Requires:         R-stats 

%description
Parameter estimation and classification for Gaussian Mixture Models (GMMs)
in the presence of missing data. This package complements existing
implementations by allowing for both missing elements in the input vectors
and full (as opposed to strictly diagonal) covariance matrices. Estimation
is performed using an expectation conditional maximization algorithm that
accounts for missingness of both the cluster assignments and the vector
components. The output includes the marginal cluster membership
probabilities; the mean and covariance of each cluster; the posterior
probabilities of cluster membership; and a completed version of the input
data, with missing values imputed to their posterior expectations. For
additional details, please see McCaw ZR, Julienne H, Aschard H. "Fitting
Gaussian mixture models on incomplete data."
<doi:10.1186/s12859-022-04740-9>.

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
