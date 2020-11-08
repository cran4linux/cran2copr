%global packname  distr6
%global packver   1.4.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.7
Release:          1%{?dist}%{?buildtag}
Summary:          The Complete R6 Probability Distributions Interface

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-R62S3 >= 1.4.0
BuildRequires:    R-CRAN-set6 >= 0.2.0
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-R62S3 >= 1.4.0
Requires:         R-CRAN-set6 >= 0.2.0
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-R6 
Requires:         R-stats 
Requires:         R-CRAN-Rcpp 

%description
An R6 object oriented distributions package. Unified interface for 42
probability distributions and 11 kernels including functionality for
multiple scientific types. Additionally functionality for composite
distributions and numerical imputation. Design patterns including wrappers
and decorators are described in Gamma et al. (1994, ISBN:0-201-63361-2).
For quick reference of probability distributions including d/p/q/r
functions and results we refer to McLaughlin, M. P. (2001). Additionally
Devroye (1986, ISBN:0-387-96305-7) for sampling the Dirichlet
distribution, Gentle (2009) <doi:10.1007/978-0-387-98144-4> for sampling
the Multivariate Normal distribution and Michael et al. (1976)
<doi:10.2307/2683801> for sampling the Wald distribution.

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
