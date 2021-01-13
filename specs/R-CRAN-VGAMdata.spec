%global packname  VGAMdata
%global packver   1.1-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Data Supporting the 'VGAM' Package

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-VGAM 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-VGAM 

%description
Mainly data sets to accompany the VGAM package and the book "Vector
Generalized Linear and Additive Models: With an Implementation in R" (Yee,
2015) <DOI:10.1007/978-1-4939-2818-7>. These are used to illustrate vector
generalized linear and additive models (VGLMs/VGAMs), and associated
models (Reduced-Rank VGLMs, Quadratic RR-VGLMs, Row-Column Interaction
Models, and constrained and unconstrained ordination models in ecology).
This package now contains some old VGAM family functions which have been
replaced by newer ones (often because they are now special cases).

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
