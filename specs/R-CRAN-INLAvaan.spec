%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  INLAvaan
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Approximate Bayesian Latent Variable Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli 
Requires:         R-graphics 
Requires:         R-CRAN-lavaan 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
Implements approximate Bayesian inference for Structural Equation Models
(SEM) using a custom adaptation of the Integrated Nested Laplace
Approximation (Rue et al., 2009) <doi:10.1111/j.1467-9868.2008.00700.x> as
described in Jamil and Rue (2026a) <doi:10.48550/arXiv.2603.25690>.
Provides a computationally efficient alternative to Markov Chain Monte
Carlo (MCMC) for Bayesian estimation, allowing users to fit latent
variable models using the 'lavaan' syntax. See also the companion paper on
implementation and workflows, Jamil and Rue (2026b)
<doi:10.48550/arXiv.2604.00671>.

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
