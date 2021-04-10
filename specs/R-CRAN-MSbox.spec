%global packname  MSbox
%global packver   1.3.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.9
Release:          1%{?dist}%{?buildtag}
Summary:          Mass Spectrometry Tools

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggfortify 
BuildRequires:    R-CRAN-plotly 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-xml2 
Requires:         R-stats 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggfortify 
Requires:         R-CRAN-plotly 

%description
Common mass spectrometry tools described in John Roboz (2013)
<doi:10.1201/b15436>. It allows checking element isotopes, calculating
(isotope labelled) exact monoisitopic mass, m/z values and mass accuracy,
and inspecting possible contaminant mass peaks, examining possible adducts
in electrospray ionization (ESI) and matrix-assisted laser desorption
ionization (MALDI) ion sources.

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
