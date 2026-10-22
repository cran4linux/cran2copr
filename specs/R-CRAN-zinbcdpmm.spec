%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  zinbcdpmm
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian ZINB-Ordinal Joint Model with CDPMM Random Effects

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-BayesLogit 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-stats 
Requires:         R-CRAN-BayesLogit 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-loo 
Requires:         R-stats 

%description
Fits a Bayesian joint model for longitudinal zero-inflated negative
binomial (ZINB) and ordinal outcomes with shared random effects under a
centered Dirichlet process mixture model (CDPMM) prior.  Provides a
blocked Gibbs sampler with Polya-Gamma (PG) and Chinese restaurant table
data augmentation, plus helpers for simulation and posterior summaries
based on the deviance information criterion (DIC), the widely applicable
information criterion (WAIC) and the leave-one-out information criterion
(LOOIC).  The PG augmentation follows Polson, Scott and Windle (2013)
<doi:10.1080/01621459.2013.829001>, the zero-inflated negative binomial
construction follows Neelon (2019) <doi:10.1214/18-BA1132>, and the
centered Dirichlet process mixture prior follows Tang, Tang and Pan (2014)
<doi:10.1016/j.csda.2014.02.015>.

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
