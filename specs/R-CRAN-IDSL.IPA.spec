%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  IDSL.IPA
%global packver   2.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.8
Release:          1%{?dist}%{?buildtag}
Summary:          Intrinsic Peak Analysis (IPA) for HRMS Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-IDSL.MXP 
BuildRequires:    R-CRAN-readxl 
Requires:         R-CRAN-IDSL.MXP 
Requires:         R-CRAN-readxl 

%description
A multi-layered untargeted pipeline for high-throughput LC/HRMS data
processing to extract signals of organic small molecules. The package
performs ion pairing, peak detection, peak table alignment, retention time
correction, aligned peak table gap filling, peak annotation and
visualization of extracted ion chromatograms (EICs) and total ion
chromatograms (TICs). The 'IDSL.IPA' package was introduced in
<doi:10.1021/acs.jproteome.2c00120> .

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
