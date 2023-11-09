%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rvMF
%global packver   0.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.8
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Generation of von Mises-Fisher Distributed Pseudo-Random Vectors

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rfast >= 2.0.6
BuildRequires:    R-CRAN-scModels >= 1.0.4
BuildRequires:    R-CRAN-Rcpp >= 1.0.10
BuildRequires:    R-CRAN-Bessel >= 0.6.0
Requires:         R-CRAN-Rfast >= 2.0.6
Requires:         R-CRAN-scModels >= 1.0.4
Requires:         R-CRAN-Rcpp >= 1.0.10
Requires:         R-CRAN-Bessel >= 0.6.0

%description
Generates pseudo-random vectors that follow an arbitrary von Mises-Fisher
distribution on a sphere. This method is fast and efficient when
generating a large number of pseudo-random vectors. Functions to generate
random variates and compute density for the distribution of an inner
product between von Mises-Fisher random vector and its mean direction are
also provided.

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
