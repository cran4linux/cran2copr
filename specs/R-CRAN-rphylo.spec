%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rphylo
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Phylogenetic Analysis with Dependent Discrete Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-stats 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-phangorn 
Requires:         R-CRAN-expm 
Requires:         R-stats 

%description
Implementation of dependent discrete models (with reversible jump MCMC)
derived from 'BayesTraits' V5.0.3
<https://github.com/AndrewPMeade/BayesTraits-Release/tree/Release>.
Original software copyright Andrew Meade and contributors, distributed
under GPL-3. Modifications for this package by Vivian G. Li
<liguo.vivian@gmail.com>. The following articles should be referenced when
using this package: Pagel, M., A. Meade and D. Barker (2004) "Bayesian
estimation of ancestral character states on phylogenies"
<doi:10.1080/10635150490522232>; Pagel, M. (1994) "Detecting correlated
evolution on phylogenies: a general method for the comparative analysis of
discrete characters" <doi:10.1098/rspb.1994.0006>; Pagel, M. and A. Meade
(2006) "Bayesian analysis of correlated evolution of discrete characters
by reversible-jump Markov chain Monte Carlo" <doi:10.1086/503444>.

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
