%global packname  ellipticalsymmetry
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Elliptical Symmetry Tests

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.4.0
Requires:         R-core >= 2.4.0
BuildArch:        noarch
BuildRequires:    R-stats >= 2.4.0
BuildRequires:    R-datasets >= 2.4.0
BuildRequires:    R-CRAN-doRNG >= 1.8.2
BuildRequires:    R-CRAN-foreach >= 1.5.1
BuildRequires:    R-CRAN-ICSNP >= 1.1.1
BuildRequires:    R-CRAN-doParallel >= 1.0.16
Requires:         R-stats >= 2.4.0
Requires:         R-datasets >= 2.4.0
Requires:         R-CRAN-doRNG >= 1.8.2
Requires:         R-CRAN-foreach >= 1.5.1
Requires:         R-CRAN-ICSNP >= 1.1.1
Requires:         R-CRAN-doParallel >= 1.0.16

%description
Given the omnipresence of the assumption of elliptical symmetry, it is
essential to be able to test whether that assumption actually holds true
or not for the data at hand. This package provides several statistical
tests for elliptical symmetry that are described in Babic et al. (2021)
<arXiv:2011.12560v2>.

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
