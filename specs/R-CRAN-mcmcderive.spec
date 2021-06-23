%global __brp_check_rpaths %{nil}
%global packname  mcmcderive
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Derive MCMC Parameters

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-chk 
BuildRequires:    R-CRAN-extras 
BuildRequires:    R-CRAN-mcmcr 
BuildRequires:    R-CRAN-nlist 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-universals 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-chk 
Requires:         R-CRAN-extras 
Requires:         R-CRAN-mcmcr 
Requires:         R-CRAN-nlist 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-universals 

%description
Generates derived parameter(s) from Monte Carlo Markov Chain (MCMC)
samples using R code. This allows Bayesian models to be fitted without the
inclusion of derived parameters which add unnecessary clutter and slow
model fitting. For more information on MCMC samples see Brooks et al.
(2011) <isbn:978-1-4200-7941-8>.

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
