%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  photobiologyPlants
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Plant Photobiology Related Functions and Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-photobiologyWavebands >= 0.5.1
BuildRequires:    R-CRAN-photobiology >= 0.10.15
Requires:         R-CRAN-photobiologyWavebands >= 0.5.1
Requires:         R-CRAN-photobiology >= 0.10.15

%description
Provides functions for quantifying visible (VIS) and ultraviolet (UV)
radiation in relation to the photoreceptors Phytochromes, Cryptochromes,
and UVR8 which are present in plants. It also includes data sets on the
optical properties of plants. Part of the 'r4photobiology' suite, Aphalo
P. J. (2015) <doi:10.19232/uv4pb.2015.1.14>.

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
