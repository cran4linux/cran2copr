%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  remstats
%global packver   3.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Computes Statistics for Relational Event History Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.8.3
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-CRAN-Rcpp >= 1.0.8.3
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Computes a variety of statistics for relational event models. Relational
event models enable researchers to investigate both exogenous and
endogenous factors influencing the evolution of a time-ordered sequence of
events. These models are categorized into tie-oriented models (Butts, C.,
2008, <doi:10.1111/j.1467-9531.2008.00203.x>), where the probability of a
dyad interacting next is modeled in a single step, and actor-oriented
models (Stadtfeld, C., & Block, P., 2017, <doi:10.15195/v4.a14>), which
first model the probability of a sender initiating an interaction and
subsequently the probability of the sender's choice of receiver. The
package is designed to compute a variety of statistics that summarize
exogenous and endogenous influences on the event stream for both types of
models.

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
