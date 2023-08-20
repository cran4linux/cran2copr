%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BiasedUrn
%global packver   2.0.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.11
Release:          1%{?dist}%{?buildtag}
Summary:          Biased Urn Model Distributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
Statistical models of biased sampling in the form of univariate and
multivariate noncentral hypergeometric distributions, including Wallenius'
noncentral hypergeometric distribution and Fisher's noncentral
hypergeometric distribution. See vignette("UrnTheory") for explanation of
these distributions. Literature: Fog, A. (2008a). Calculation Methods for
Wallenius' Noncentral Hypergeometric Distribution, Communications in
Statistics, Simulation and Computation, 37(2)
<doi:10.1080/03610910701790269>. Fog, A. (2008b). Sampling methods for
Wallenius’ and Fisher’s noncentral hypergeometric distributions,
Communications in Statistics—Simulation and Computation, 37(2)
<doi:10.1080/03610910701790236>.

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
