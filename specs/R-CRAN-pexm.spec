%global packname  pexm
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Loading a JAGS Module for the Piecewise Exponential Distribution

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-CRAN-msm 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-rjags 
Requires:         R-CRAN-msm 

%description
Load the Just Another Gibbs Sampling (JAGS) module 'pexm'. The module
provides the tools to work with the Piecewise Exponential (PE)
distribution in a Bayesian model with the corresponding Markov Chain Monte
Carlo algorithm (Gibbs Sampling) implemented via JAGS. Details about the
module implementation can be found in Mayrink et al. (2020)
<arXiv:2004.12359>.

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
