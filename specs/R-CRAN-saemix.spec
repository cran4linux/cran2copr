%global __brp_check_rpaths %{nil}
%global packname  saemix
%global packver   3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Stochastic Approximation Expectation Maximization (SAEM) Algorithm

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-npde >= 3.2
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-npde >= 3.2
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-rlang 

%description
The 'saemix' package implements the Stochastic Approximation EM algorithm
for parameter estimation in (non)linear mixed effects models. The SAEM
algorithm (i) computes the maximum likelihood estimator of the population
parameters, without any approximation of the model (linearisation,
quadrature approximation,...), using the Stochastic Approximation
Expectation Maximization (SAEM) algorithm, (ii) provides standard errors
for the maximum likelihood estimator (iii) estimates the conditional
modes, the conditional means and the conditional standard deviations of
the individual parameters, using the Hastings-Metropolis algorithm (see
Comets et al. (2017) <doi:10.18637/jss.v080.i03>). Many applications of
SAEM in agronomy, animal breeding and PKPD analysis have been published by
members of the Monolix group. The full PDF documentation for the package
including references about the algorithm and examples can be downloaded on
the github of the IAME research institute for 'saemix':
<https://github.com/iame-researchCenter/saemix/blob/7638e1b09ccb01cdff173068e01c266e906f76eb/docsaem.pdf>.

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
