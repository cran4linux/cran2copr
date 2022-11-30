%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  IFC
%global packver   0.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Imaging Flow Cytometry

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-Rcpp >= 0.10.0
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-tiff 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-utils 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-gridGraphics 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-KernSmooth 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-visNetwork 
Requires:         R-CRAN-Rcpp >= 0.10.0
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-png 
Requires:         R-CRAN-tiff 
Requires:         R-CRAN-jpeg 
Requires:         R-utils 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-gridGraphics 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-KernSmooth 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-visNetwork 

%description
Contains several tools to treat imaging flow cytometry data from
'ImageStream®' and 'FlowSight®' cytometers ('Amnis®', part of 'Luminex®').
Provides an easy and simple way to read and write .fcs, .rif, .cif and
.daf files. Information such as masks, features, regions and populations
set within these files can be retrieved for each single cell. In addition,
raw data such as images stored can also be accessed. Users, may hopefully
increase their productivity thanks to dedicated functions to extract,
visualize, manipulate and export 'IFC' data. Toy data example can be
installed through the 'IFCdata' package of approximately 32 MB, which is
available in a 'drat' repository <https://gitdemont.github.io/IFCdata/>.
See file 'COPYRIGHTS' and file 'AUTHORS' for a list of copyright holders
and authors.

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
