%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  glinvci
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Phylogenetic Comparative Methods with Uncertainty Estimates

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-lbfgsb3c 
BuildRequires:    R-CRAN-BB 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-lbfgsb3c 
Requires:         R-CRAN-BB 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-generics 
Requires:         R-utils 
Requires:         R-stats 

%description
A framework for analytically computing the asymptotic confidence intervals
and maximum-likelihood estimates of a class of continuous-time Gaussian
branching processes defined by Mitov V, Bartoszek K, Asimomitis G, Stadler
T (2019) <doi:10.1016/j.tpb.2019.11.005>. The class of model includes the
widely used Ornstein-Uhlenbeck and Brownian motion branching processes.
The framework is designed to be flexible enough so that the users can
easily specify their own sub-models, or re-parameterizations, and obtain
the maximum-likelihood estimates and confidence intervals of their own
custom models.

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
