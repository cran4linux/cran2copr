%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ttdo
%global packver   0.0.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.10
Release:          1%{?dist}%{?buildtag}
Summary:          Extend 'tinytest' with 'diffobj' and 'tinysnapshot'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tinytest >= 1.4.1
BuildRequires:    R-CRAN-tinysnapshot >= 0.0.8
BuildRequires:    R-CRAN-diffobj 
BuildRequires:    R-CRAN-base64enc 
Requires:         R-CRAN-tinytest >= 1.4.1
Requires:         R-CRAN-tinysnapshot >= 0.0.8
Requires:         R-CRAN-diffobj 
Requires:         R-CRAN-base64enc 

%description
The 'tinytest' package offers a light-weight zero-dependency unit-testing
framework to which this package adds support via the 'diffobj' package for
'diff'-style textual comparison of R objects, as well as via
'tinysnapshot' package for visual differences in plots.

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
