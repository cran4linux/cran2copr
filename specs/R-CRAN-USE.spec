%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  USE
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Uniform Sampling of the Environmental Space

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-cowplot 
Requires:         R-CRAN-sf 
Requires:         R-parallel 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-cowplot 

%description
Provides functions for uniform sampling of the environmental space,
designed to assist species distribution modellers in gathering
ecologically relevant pseudo-absence data. The method ensures balanced
representation of environmental conditions and helps reduce sampling bias
in model calibration. Based on the framework described by Da Re et al.
(2023) <doi:10.1111/2041-210X.14209>.

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
