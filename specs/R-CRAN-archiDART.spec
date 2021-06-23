%global __brp_check_rpaths %{nil}
%global packname  archiDART
%global packver   3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.4
Release:          1%{?dist}%{?buildtag}
Summary:          Plant Root System Architecture Analysis Using DART and RSML Files

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-sp 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-gtools 
Requires:         R-grDevices 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-sp 

%description
Analysis of complex plant root system architectures (RSA) using the output
files created by Data Analysis of Root Tracings (DART), an open-access
software dedicated to the study of plant root architecture and development
across time series (Le Bot et al (2010) "DART: a software to analyse root
system architecture and development from captured images", Plant and Soil,
<DOI:10.1007/s11104-009-0005-2>), and RSA data encoded with the Root
System Markup Language (RSML) (Lobet et al (2015) "Root System Markup
Language: toward a unified root architecture description language", Plant
Physiology, <DOI:10.1104/pp.114.253625>). More information can be found in
Delory et al (2016) "archiDART: an R package for the automated computation
of plant root architectural traits", Plant and Soil,
<DOI:10.1007/s11104-015-2673-4>.

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
