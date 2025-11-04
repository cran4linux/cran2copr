%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MixStable
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Parameter Estimation for Stable Distributions and Their Mixtures

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-stabledist 
BuildRequires:    R-CRAN-mixtools 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-libstable4u 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-utils 
Requires:         R-CRAN-stabledist 
Requires:         R-CRAN-mixtools 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-libstable4u 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-MASS 
Requires:         R-utils 

%description
Provides various functions for parameter estimation of one-dimensional
stable distributions and their mixtures. It implements a diverse set of
estimation methods, including quantile-based approaches, regression
methods based on the empirical characteristic function (empirical, kernel,
and recursive), and maximum likelihood estimation. For mixture models, it
provides stochastic expectation–maximization (SEM) algorithms and Bayesian
estimation methods using sampling and importance sampling to overcome the
long burn-in period of Markov Chain Monte Carlo (MCMC) strategies. The
package also includes tools and statistical tests for analyzing whether a
dataset follows a stable distribution. Some of the implemented methods are
described in Hajjaji, O., Manou-Abi, S. M., and Slaoui, Y. (2024)
<doi:10.1080/02664763.2024.2434627>.

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
