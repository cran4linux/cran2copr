%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  binaryMM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Flexible Marginalized Models for Binary Correlated Outcomes

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-fastGHQuad 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-fastGHQuad 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Rcpp 

%description
Estimates marginalized mean and dependence model parameters for correlated
binary response data. Dependence model may include transition and/or
latent variable terms. Methods are described in: Heagerty (1999)
<doi:10.1111/j.0006-341x.1999.00688.x>, Heagerty (2002)
<doi:10.1111/j.0006-341x.2002.00342.x>, Schildcrout and Heagerty (2007)
<doi:10.1111/j.1541-0420.2006.00680.x>.

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
