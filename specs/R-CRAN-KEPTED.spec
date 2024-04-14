%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  KEPTED
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Kernel-Embedding-of-Probability Test for Elliptical Distribution

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-CompQuadForm 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-stats 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-CompQuadForm 
Requires:         R-CRAN-cubature 
Requires:         R-stats 

%description
Provides an implementation of a kernel-embedding of probability test for
elliptical distribution. This is an asymptotic test for elliptical
distribution under general alternatives, and the location and shape
parameters are assumed to be unknown. Some side-products are posted,
including the transformation between rectangular and polar coordinates and
two product-type kernel functions. See Tang and Li (2024)
<doi:10.48550/arXiv.2306.10594> for details.

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
