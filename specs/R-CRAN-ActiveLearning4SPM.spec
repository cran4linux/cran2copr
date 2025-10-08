%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ActiveLearning4SPM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Active Learning for Process Monitoring

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-mvnfast 
Requires:         R-CRAN-rrcov 
Requires:         R-CRAN-caTools 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-pROC 
Requires:         R-stats 

%description
Implements the methodology introduced in Capezza, Lepore, and Paynabar
(2025) <doi:10.1080/00401706.2025.2561744> for process monitoring with
limited labeling resources. The package provides functions to (i) simulate
data streams with true latent states and multivariate Gaussian
observations as done in the paper, (ii) fit partially hidden Markov models
(pHMMs) using a constrained Baum-Welch algorithm with partial labels, and
(iii) perform stream-based active learning that balances exploration and
exploitation to decide whether to request labels in real time. The
methodology is particularly suited for statistical process monitoring in
industrial applications where labeling is costly.

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
