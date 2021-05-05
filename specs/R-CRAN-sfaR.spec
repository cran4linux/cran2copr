%global packname  sfaR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Stochastic Frontier Analysis using R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-emdbook 
BuildRequires:    R-CRAN-fBasics 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-CRAN-marqLevAlg 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-primes 
BuildRequires:    R-CRAN-qrng 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-trustOptim 
BuildRequires:    R-CRAN-ucminf 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-emdbook 
Requires:         R-CRAN-fBasics 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-gsl 
Requires:         R-CRAN-marqLevAlg 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-maxLik 
Requires:         R-methods 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-primes 
Requires:         R-CRAN-qrng 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-trustOptim 
Requires:         R-CRAN-ucminf 

%description
Maximum likelihood estimation for stochastic frontier analysis (SFA) of
production (profit) and cost functions. The package includes several
distributions for the one-sided error term (i.e. Rayleigh, Gamma, Weibull,
lognormal, uniform, generalized exponential and truncated skewed Laplace)
as well as the latent class stochastic frontier model (LCM) as described
in Dakpo et al. (2021) <doi:10.1111/1477-9552.12422>. Several
possibilities in terms of optimization algorithms are proposed.

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
