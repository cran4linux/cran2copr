%global __brp_check_rpaths %{nil}
%global packname  chkptstanr
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Checkpoint MCMC Sampling with 'Stan'

License:          Apache License 2.0 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-brms >= 2.16.1
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-brms >= 2.16.1
Requires:         R-CRAN-abind 
Requires:         R-methods 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-rstan 
Requires:         R-CRAN-rstantools

%description
Fit Bayesian models in Stan <doi: 10.18637/jss.v076.i01> with
checkpointing, that is, the ability to stop the MCMC sampler at will, and
then pick right back up where the MCMC sampler left off. Custom 'Stan'
models can be fitted, or the popular package 'brms' <doi:
10.18637/jss.v080.i01> can be used to generate the 'Stan' code. This
package is fully compatible with the R packages 'brms', 'posterior',
'cmdstanr', and 'bayesplot'.

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
