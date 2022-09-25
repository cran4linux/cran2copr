%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesianMediationA
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Mediation Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.1
Requires:         R-core >= 2.14.1
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-R2jags 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-splines 
BuildRequires:    R-methods 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-R2jags 
Requires:         R-CRAN-car 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-lattice 
Requires:         R-splines 
Requires:         R-methods 

%description
We perform general mediation analysis in the Bayesian setting using the
methods described in Yu and Li (2022, ISBN:9780367365479). With the
package, the mediation analysis can be performed on different types of
outcomes (e.g., continuous, binary, categorical, or time-to-event), with
default or user-defined priors and predictive models. The Bayesian
estimates and credible sets of mediation effects are reported as analytic
results.

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
