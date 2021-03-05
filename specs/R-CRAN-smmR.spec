%global packname  smmR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simulation, Estimation and Reliability of Semi-Markov Models

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-seqinr 
BuildRequires:    R-CRAN-DiscreteWeibull 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-seqinr 
Requires:         R-CRAN-DiscreteWeibull 
Requires:         R-CRAN-MASS 
Requires:         R-graphics 
Requires:         R-CRAN-Rcpp 

%description
Performs parametric and non-parametric estimation and simulation for
multi-state discrete-time semi-Markov processes. For the parametric
estimation, several discrete distributions are considered for the sojourn
times: Uniform, Geometric, Poisson, Discrete Weibull and Negative
Binomial. The non-parametric estimation concerns the sojourn time
distributions, where no assumptions are done on the shape of
distributions. Moreover, the estimation can be done on the basis of one or
several sample paths, with or without censoring at the beginning or/and at
the end of the sample paths. Reliability indicators such as reliability,
maintainability, availability, BMP-failure rate, RG-failure rate, mean
time to failure and mean time to repair are available as well. The
implemented methods are described in Barbu, V.S., Limnios, N. (2008)
<doi:10.1007/978-0-387-73173-5>, Barbu, V.S., Limnios, N. (2008)
<doi:10.1080/10485250701261913> and Trevezas, S., Limnios, N. (2011)
<doi:10.1080/10485252.2011.555543>. Estimation and simulation of
discrete-time k-th order Markov chains are also considered.

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
