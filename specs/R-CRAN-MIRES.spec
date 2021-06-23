%global __brp_check_rpaths %{nil}
%global packname  MIRES
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Measurement Invariance Assessment Using Random Effects Models and Shrinkage

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-stats >= 3.4.0
BuildRequires:    R-parallel >= 3.4.0
BuildRequires:    R-CRAN-nlme >= 3.1
BuildRequires:    R-CRAN-pracma >= 2.2.9
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-logspline >= 2.1.0
BuildRequires:    R-CRAN-rstantools >= 2.0.0
BuildRequires:    R-CRAN-cubature >= 2.0.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-Formula >= 1.2.1
BuildRequires:    R-CRAN-mvtnorm >= 1.0
BuildRequires:    R-CRAN-truncnorm >= 1.0
BuildRequires:    R-CRAN-dirichletprocess >= 0.4.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-HDInterval >= 0.2.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rstantools
Requires:         R-stats >= 3.4.0
Requires:         R-parallel >= 3.4.0
Requires:         R-CRAN-nlme >= 3.1
Requires:         R-CRAN-pracma >= 2.2.9
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-logspline >= 2.1.0
Requires:         R-CRAN-rstantools >= 2.0.0
Requires:         R-CRAN-cubature >= 2.0.0
Requires:         R-CRAN-Formula >= 1.2.1
Requires:         R-CRAN-mvtnorm >= 1.0
Requires:         R-CRAN-truncnorm >= 1.0
Requires:         R-CRAN-dirichletprocess >= 0.4.0
Requires:         R-CRAN-HDInterval >= 0.2.2
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 
Requires:         R-CRAN-rstantools

%description
Estimates random effect latent measurement models, wherein the loadings,
residual variances, intercepts, latent means, and latent variances all
vary across groups. The random effect variances of the measurement
parameters are then modeled using a hierarchical inclusion model, wherein
the inclusion of the variances (i.e., whether it is effectively zero or
non-zero) is informed by similar parameters (of the same type, or of the
same item). This additional hierarchical structure allows the evidence in
favor of partial invariance to accumulate more quickly, and yields more
certain decisions about measurement invariance. Martin, Williams, and Rast
(2020) <doi:10.31234/osf.io/qbdjt>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
