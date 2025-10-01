%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  coglyphr
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Compute Glyph Centers of Gravity from Image Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-imager 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-imager 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-sp 

%description
Computes the center of gravity (COG) of character-like binary images using
three different methods. This package provides functions for estimating
stroke-based, contour-based, and potential energy-based COG. It is useful
for analyzing glyph structure in areas such as visual cognition research
and font development. The contour-based method was originally proposed by
Kotani et al. (2004) <https://ipsj.ixsq.nii.ac.jp/records/36793> and
Kotani (2011) <https://shonan-it.repo.nii.ac.jp/records/2000243>, while
the potential energy-based method was introduced by Kotani et al. (2006)
<doi:10.11371/iieej.35.296>.

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
