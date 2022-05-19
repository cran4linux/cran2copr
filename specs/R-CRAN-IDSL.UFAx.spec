%global __brp_check_rpaths %{nil}
%global packname  IDSL.UFAx
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Exhaustive Chemical Enumeration for United Formula Annotation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-IDSL.IPA >= 1.5
BuildRequires:    R-CRAN-IDSL.MXP >= 1.2
BuildRequires:    R-CRAN-IDSL.UFA >= 1.2
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-RNetCDF 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-RcppAlgos 
Requires:         R-CRAN-IDSL.IPA >= 1.5
Requires:         R-CRAN-IDSL.MXP >= 1.2
Requires:         R-CRAN-IDSL.UFA >= 1.2
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-RNetCDF 
Requires:         R-CRAN-base64enc 
Requires:         R-stats 
Requires:         R-CRAN-readxl 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-RcppAlgos 

%description
A pipeline to annotate a number of peaks from the IDSL.IPA peaklists using
an exhaustive chemical enumeration-based approach. This package can
perform elemental composition using following 15 elements : C, B, Br, Cl,
K, S, Se, Si, N, H, As, F, I, Na, O, and P.

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
