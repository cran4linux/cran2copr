%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  alphaci
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Confidence Intervals for Coefficient Alpha and Standardized Alpha

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-matrixcalc 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-matrixcalc 

%description
Calculate confidence intervals for alpha and standardized alpha using
asymptotic theory or the studentized bootstrap, with or without
transformations. Supports the asymptotic distribution-free method of
Maydeu-Olivares, et al. (2007) <doi:10.1037/1082-989X.12.2.157>, the
pseudo-elliptical method of Yuan & Bentler (2002)
<doi:10.1007/BF02294845>, and the normal method of van Zyl et al. (1999)
<doi:10.1007/BF02296146>, for both coefficient alpha and standardized
alpha.

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
