%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geotargets
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          'targets' Extensions for Geographic Spatial Formats

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.2
BuildRequires:    R-CRAN-withr >= 3.0.0
BuildRequires:    R-CRAN-gdalraster >= 2.0.0
BuildRequires:    R-CRAN-terra >= 1.8.10
BuildRequires:    R-CRAN-targets >= 1.8.0
BuildRequires:    R-CRAN-rlang >= 1.1.3
BuildRequires:    R-CRAN-zip 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-cli >= 3.6.2
Requires:         R-CRAN-withr >= 3.0.0
Requires:         R-CRAN-gdalraster >= 2.0.0
Requires:         R-CRAN-terra >= 1.8.10
Requires:         R-CRAN-targets >= 1.8.0
Requires:         R-CRAN-rlang >= 1.1.3
Requires:         R-CRAN-zip 
Requires:         R-CRAN-lifecycle 

%description
Provides extensions for various geographic spatial file formats, such as
shape files and rasters. Currently provides support for the 'terra'
geographic spatial formats. See the vignettes for worked examples,
demonstrations, and explanations of how to use the various package
extensions.

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
