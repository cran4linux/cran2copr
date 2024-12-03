%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OpenRepGrid
%global packver   0.1.16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.16
Release:          1%{?dist}%{?buildtag}
Summary:          Tools to Analyze Repertory Grid Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-grid 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-pvclust 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-igraph 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-grid 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-pvclust 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-igraph 

%description
Analyze repertory grids, a qualitative-quantitative data collection
technique devised by George A. Kelly in the 1950s. Today, grids are used
across various domains ranging from clinical psychology to marketing. The
package contains functions to quantitatively analyze and visualize
repertory grid data (e.g. 'Fransella', 'Bell', & 'Bannister', 2004, ISBN:
978-0-470-09080-0). The package is part of the The package is part of the
<https://openrepgrid.org/> project.

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
