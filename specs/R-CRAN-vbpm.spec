%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vbpm
%global packver   0.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.1
Release:          1%{?dist}%{?buildtag}
Summary:          Variational Bayes Psychometric Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-MASS 
Requires:         R-stats 

%description
Variational Bayes estimation for a family of psychometric measurement
models. Two models are provided. Variational Bayes factor analysis (vbfa)
is a regularized partially confirmatory factor model spanning the
confirmatory-exploratory continuum via spike-and-slab priors on the
loadings (Chen, Guo, Zhang, and Pan, 2021 <doi:10.1037/met0000293>; Chen,
2023 <doi:10.3758/s13428-022-01884-7>; Jin and Chen, 2025
<doi:10.1080/10705511.2024.2432612>), with an optional dynamic
(warm-started) regularization path, an orthogonal bifactor
parameterization, and optional sparse residual (local dependence)
estimation through a graphical spike-and-slab prior solved by QUIC (Jin,
Chen, Yan, and Zhang, 2026 <doi:10.31234/osf.io/dehtv_v2>). Regularized
MIMIC (vbmimic) extends this to multiple-indicators multiple-causes
models, placing spike-and-slab priors on both the measurement and the
structural part (Jin and Chen, 2025 <doi:10.1080/00273171.2025.2483253>).
Companion tools compute SEM-like fit statistics, and sweep a factor-count
window to report candidate fit, criterion, and between-candidate
loading-correspondence measurements without selecting a count (Chen and
Jin, 2026 <doi:10.48550/arXiv.2607.07159>). Data generators for either
model family are also provided.

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
