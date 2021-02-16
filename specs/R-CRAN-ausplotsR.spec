%global packname  ausplotsR
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          TERN AusPlots Analysis Package

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-mapdata 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-simba 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-jose 
BuildRequires:    R-CRAN-betapart 
BuildRequires:    R-CRAN-curl 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-mapdata 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-simba 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-jose 
Requires:         R-CRAN-betapart 
Requires:         R-CRAN-curl 

%description
Extraction, preparation, visualisation and analysis of TERN AusPlots
ecosystem monitoring data. Direct access to plot-based data on vegetation
and soils across Australia, including physical sample barcode numbers.
Simple function calls extract the data and merge them into species
occurrence matrices for downstream analysis, or calculate things like
basal area and fractional cover. TERN AusPlots is a national field
plot-based ecosystem surveillance monitoring method and dataset for
Australia. The data have been collected across a national network of plots
and transects by the Terrestrial Ecosystem Research Network (TERN -
<https://www.tern.org.au>), an Australian Government NCRIS-enabled
project, and its Ecosystem Surveillance platform
(<https://www.tern.org.au/tern-observatory/tern-ecosystem-surveillance/>).

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
