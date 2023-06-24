%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  flexmsm
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          A General Framework for Flexible Multi-State Survival Modelling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-GJRM 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-trust 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-parallel 
Requires:         R-CRAN-GJRM 
Requires:         R-CRAN-mgcv 
Requires:         R-stats 
Requires:         R-CRAN-trust 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-matrixStats 
Requires:         R-parallel 

%description
A general estimation framework for multi-state Markov processes with
flexible specification of the transition intensities. The log-transition
intensities can be specified through Generalised Additive Models which
allow for virtually any type of covariate effect. Elementary
specifications such as time-homogeneous processes and simple parametric
forms are also supported. There are no limitations on the type of process
one can assume, with both forward and backward transitions allowed and
virtually any number of states.

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
