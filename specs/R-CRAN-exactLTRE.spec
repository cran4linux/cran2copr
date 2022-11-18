%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  exactLTRE
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          An Exact Method for Life Table Response Experiment (LTRE) Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-popdemo 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-popdemo 

%description
Life Table Response Experiments (LTREs) are a method of comparative
demographic analysis. The purpose is to quantify how the difference or
variance in vital rates (stage-specific survival, growth, and fertility)
among populations contributes to difference or variance in the population
growth rate, "lambda." We provide functions for one-way fixed design and
random design LTRE, using either the classical methods that have been in
use for several decades, or an fANOVA-based exact method that directly
calculates the impact on lambda of changes in matrix elements, for matrix
elements and their interactions. The equations and descriptions for the
classical methods of LTRE analysis can be found in "Matrix Population
Models: Construction, Analysis, and Interpretation (2nd edition)" Caswell
(2001, ISBN: 0878930965), and the fANOVA-based exact methods will be
published in a forthcoming paper. We also provide some demographic
functions, including generation time from Bienvenu and Legendre (2015)
<doi:10.1086/681104>. For implementation of exactLTRE where all possible
interactions are calculated, we use an operator matrix presented in
Poelwijk, Krishna, and Ranganathan (2016)
<doi:10.1371/journal.pcbi.1004771>.

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
