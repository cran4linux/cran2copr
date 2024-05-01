%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  psborrow2
%global packver   0.0.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3.4
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Dynamic Borrowing Analysis and Simulation

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-posterior 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-simsurv 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-glue 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-CRAN-posterior 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-future 
Requires:         R-CRAN-simsurv 

%description
Bayesian dynamic borrowing is an approach to incorporating external data
to supplement a randomized, controlled trial analysis in which external
data are incorporated in a dynamic way (e.g., based on similarity of
outcomes); see Viele 2013 <doi:10.1002/pst.1589> for an overview. This
package implements the hierarchical commensurate prior approach to dynamic
borrowing as described in Hobbes 2011
<doi:10.1111/j.1541-0420.2011.01564.x>. There are three main
functionalities. First, 'psborrow2' provides a user-friendly interface for
applying dynamic borrowing on the study results handles the Markov Chain
Monte Carlo sampling on behalf of the user. Second, 'psborrow2' provides a
simulation framework to compare different borrowing parameters (e.g. full
borrowing, no borrowing, dynamic borrowing) and other trial and borrowing
characteristics (e.g. sample size, covariates) in a unified way. Third,
'psborrow2' provides a set of functions to generate data for simulation
studies, and also allows the user to specify their own data generation
process. This package is designed to use the sampling functions from
'cmdstanr' which can be installed from <https://mc-stan.org/r-packages/>.

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
