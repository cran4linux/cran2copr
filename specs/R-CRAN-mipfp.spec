%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mipfp
%global packver   3.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Multidimensional Iterative Proportional Fitting and Alternative Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cmm 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-cmm 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-numDeriv 

%description
An implementation of the iterative proportional fitting (IPFP), maximum
likelihood, minimum chi-square and weighted least squares procedures for
updating a N-dimensional array with respect to given target marginal
distributions (which, in turn can be multidimensional). The package also
provides an application of the IPFP to simulate multivariate Bernoulli
distributions.

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
