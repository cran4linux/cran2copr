%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SSLfmm
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Semi-Supervised Learning under a Mixed-Missingness Mechanism in Finite Mixture Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-matrixStats 
Requires:         R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-matrixStats 

%description
Implements a semi-supervised learning framework for finite mixture models
under a mixed-missingness mechanism. The approach models both missing
completely at random (MCAR) and entropy-based missing at random (MAR)
processes using a logistic–entropy formulation. Estimation is carried out
via an Expectation–-Conditional Maximisation (ECM) algorithm with robust
initialisation routines for stable convergence. The methodology relates to
the statistical perspective and informative missingness behaviour
discussed in Ahfock and McLachlan (2020) <doi:10.1007/s11222-020-09971-5>
and Ahfock and McLachlan (2023) <doi:10.1016/j.ecosta.2022.03.007>. The
package provides functions for data simulation, model estimation,
prediction, and theoretical Bayes error evaluation for analysing partially
labelled data under a mixed-missingness mechanism.

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
