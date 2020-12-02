%global packname  gfilmm
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Fiducial Inference for Normal Linear Mixed Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-rgr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-lazyeval 
Requires:         R-stats 
Requires:         R-CRAN-spatstat 
Requires:         R-utils 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-rgr 
Requires:         R-CRAN-Matrix 
Requires:         R-parallel 

%description
Simulation of the generalized fiducial distribution for normal linear
mixed models with interval data. Fiducial inference is somehow similar to
Bayesian inference, in the sense that it is based on a distribution that
represents the uncertainty about the parameters, like the posterior
distribution in Bayesian statistics. It does not require a prior
distribution, and it yields results close to frequentist results.
Reference: Cisewski and Hannig (2012) <doi:10.1214/12-AOS1030>.

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
