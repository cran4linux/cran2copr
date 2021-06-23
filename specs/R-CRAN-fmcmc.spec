%global __brp_check_rpaths %{nil}
%global packname  fmcmc
%global packver   0.4-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          A friendly MCMC framework

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
Requires:         R-parallel 
Requires:         R-CRAN-coda 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-MASS 
Requires:         R-Matrix 

%description
Provides a friendly (flexible) Markov Chain Monte Carlo (MCMC) framework
for implementing Metropolis-Hastings algorithm in a modular way allowing
users to specify automatic convergence checker, personalized transition
kernels, and out-of-the-box multiple MCMC chains using parallel computing.
Most of the methods implemented in this package can be found in Brooks et
al. (2011, ISBN 9781420079425). Among the methods included, we have:
Haario (2001) <doi:10.1007/s11222-011-9269-5> Adaptive Metropolis, Vihola
(2012) <doi:10.1007/s11222-011-9269-5> Robust Adaptive Metropolis, and
Thawornwattana et al. (2018) <doi:10.1214/17-BA1084> Mirror transition
kernels.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
