%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FastGaSP
%global packver   0.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.2
Release:          1%{?dist}%{?buildtag}
Summary:          Fast and Exact Computation of Gaussian Stochastic Process

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rstiefel 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rstiefel 

%description
Implements fast and exact computation of Gaussian stochastic process with
the Matern kernel using forward filtering and backward smoothing
algorithm. It includes efficient implementations of the inverse Kalman
filter, with applications such as estimating particle interaction
functions. These tools support models with or without noise. Additionally,
the package offers algorithms for fast parameter estimation in latent
factor models, where the factor loading matrix is orthogonal, and latent
processes are modeled by Gaussian processes.  See the references: 1)
Mengyang Gu and Yanxun Xu (2020), Journal of Computational and Graphical
Statistics; 2) Xinyi Fang and Mengyang Gu (2024),
<doi:10.48550/arXiv.2407.10089>; 3) Mengyang Gu and Weining Shen (2020),
Journal of Machine Learning Research; 4) Yizi Lin, Xubo Liu, Paul Segall
and Mengyang Gu (2025), <doi:10.48550/arXiv.2501.01324>.

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
