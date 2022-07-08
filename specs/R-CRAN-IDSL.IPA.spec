%global __brp_check_rpaths %{nil}
%global packname  IDSL.IPA
%global packver   1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9
Release:          1%{?dist}%{?buildtag}
Summary:          Intrinsic Peak Analysis (IPA) for HRMS Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-IDSL.MXP >= 1.4
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-RNetCDF 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-png 
Requires:         R-CRAN-IDSL.MXP >= 1.4
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-RNetCDF 
Requires:         R-CRAN-base64enc 
Requires:         R-grid 
Requires:         R-CRAN-readxl 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-png 

%description
A sophisticated pipeline for processing LC/HRMS data to extract signals of
organic compounds. The package performs isotope pairing, peak detection,
alignment, RT correction, gap filling, peak annotation and visualization
of extracted ion chromatograms and total ion chromatograms.

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
