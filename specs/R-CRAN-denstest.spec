%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  denstest
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Density Equality Testing

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Methods for testing the equality between groups of estimated density
functions. The package implements FDET (Fourier-based Density Equality
Testing) and MDET (Moment-based Density Equality Testing), two new
approaches introduced by the author. Both methods extend an earlier
testing approach by Delicado (2007), "Functional k-sample problem when
data are density functions" <doi:10.1007/s00180-007-0047-y>, which is
referred to as DET (Density Equality Testing) in this package for clarity.
FDET compares groups of densities based on their global shape using
Fourier transforms, while MDET tests for differences in distributional
moments. All methods are described in Anarat, Krutmann and Schwender
(2025), "Testing for Differences in Extrinsic Skin Aging Based on Density
Functions" (Submitted).

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
