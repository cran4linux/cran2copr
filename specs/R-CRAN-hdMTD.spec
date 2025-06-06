%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hdMTD
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Inference for High-Dimensional Mixture Transition Distribution Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
Requires:         R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 

%description
Estimates parameters in Mixture Transition Distribution (MTD) models, a
class of high-order Markov chains. The set of relevant pasts (lags) is
selected using either the Bayesian Information Criterion or the Forward
Stepwise and Cut algorithms. Other model parameters (e.g. transition
probabilities and oscillations) can be estimated via maximum likelihood
estimation or the Expectation-Maximization algorithm. Additionally,
'hdMTD' includes a perfect sampling algorithm that generates samples of an
MTD model from its invariant distribution. For theory, see Ost & Takahashi
(2023) <http://jmlr.org/papers/v24/22-0266.html>.

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
