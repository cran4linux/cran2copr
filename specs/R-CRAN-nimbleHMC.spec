%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nimbleHMC
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Hamiltonian Monte Carlo and Other Gradient-Based MCMC Sampling Algorithms for 'nimble'

License:          BSD_3_clause + file LICENSE | GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nimble >= 1.0.0
BuildRequires:    R-methods 
Requires:         R-CRAN-nimble >= 1.0.0
Requires:         R-methods 

%description
Provides gradient-based MCMC sampling algorithms for use with the MCMC
engine provided by the 'nimble' package.  This includes Hamiltonian Monte
Carlo (HMC) and (under development) Langevin samplers.  The HMC sampler
dynamically determines step size and number of leapfrog steps using the
No-U-Turn (NUTS) algorithm as described in Hoffman and Gelman (2014)
<arXiv:1111.4246>.  In addition, convenience functions are provided for
generating and modifying MCMC configuration objects which employ HMC
sampling.

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
