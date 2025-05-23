%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sharpshootR
%global packver   2.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          A Soil Survey Toolkit

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-aqp 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-soilDB 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-circular 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-grid 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-aqp 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-soilDB 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-circular 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-curl 
Requires:         R-grid 

%description
A collection of data processing, visualization, and export functions to
support soil survey operations. Many of the functions build on the
`SoilProfileCollection` S4 class provided by the aqp package, extending
baseline visualization to more elaborate depictions in the context of
spatial and taxonomic data. While this package is primarily developed by
and for the USDA-NRCS, in support of the National Cooperative Soil Survey,
the authors strive for generalization sufficient to support any soil
survey operation. Many of the included functions are used by the SoilWeb
suite of websites and movile applications. These functions are provided
here, with additional documentation, to enable others to replicate high
quality versions of these figures for their own purposes.

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
