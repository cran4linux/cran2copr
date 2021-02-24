%global packname  saemix
%global packver   2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Stochastic Approximation Expectation Maximization (SAEM) Algorithm

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-methods 

%description
The SAEMIX package implements the Stochastic Approximation EM algorithm
for parameter estimation in (non)linear mixed effects models. The SAEM
algorithm: - computes the maximum likelihood estimator of the population
parameters, without any approximation of the model (linearisation,
quadrature approximation,...), using the Stochastic Approximation
Expectation Maximization (SAEM) algorithm, - provides standard errors for
the maximum likelihood estimator - estimates the conditional modes, the
conditional means and the conditional standard deviations of the
individual parameters, using the Hastings-Metropolis algorithm. Several
applications of SAEM in agronomy, animal breeding and PKPD analysis have
been published by members of the Monolix group. Documentation about
'saemix' is provided by a comprehensive user guide in the inst folder, and
a reference concerning the methods is the paper by Comets, Lavenu and
Lavielle (2017, <doi:10.18637/jss.v080.i03>). See 'citation("saemix")' for
details.

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
