%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dapper
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Data Augmentation for Private Posterior Estimation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-bayesplot 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-posterior 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-stats 
Requires:         R-CRAN-bayesplot 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-posterior 
Requires:         R-CRAN-progressr 
Requires:         R-stats 

%description
A data augmentation based sampler for conducting privacy-aware Bayesian
inference. The dapper_sample() function takes an existing sampler as input
and automatically constructs a privacy-aware sampler. The process of
constructing a sampler is simplified through the specification of four
independent modules, allowing for easy comparison between different
privacy mechanisms by only swapping out the relevant modules. Probability
mass functions for the discrete Gaussian and discrete Laplacian are
provided to facilitate analyses dealing with privatized count data. The
output of dapper_sample() can be analyzed using many of the same tools
from the 'rstan' ecosystem. For methodological details on the sampler see
Ju et al. (2022) <doi:10.48550/arXiv.2206.00710>, and for details on the
discrete Gaussian and discrete Laplacian distributions see Canonne et al.
(2020) <doi:10.48550/arXiv.2004.00010>.

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
