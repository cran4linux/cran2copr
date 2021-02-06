%global packname  coreCT
%global packver   1.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Programmatic Analysis of Sediment Cores Using Computed Tomography Imaging

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-oro.dicom 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-oro.dicom 
Requires:         R-CRAN-plyr 

%description
Computed tomography (CT) imaging is a powerful tool for understanding the
composition of sediment cores. This package streamlines and accelerates
the analysis of CT data generated in the context of environmental science.
Included are tools for processing raw DICOM images to characterize
sediment composition (sand, peat, etc.). Root analyses are also enabled,
including measures of external surface area and volumes for user-defined
root size classes. For a detailed description of the application of
computed tomography imaging for sediment characterization, see: Davey, E.,
C. Wigand, R. Johnson, K. Sundberg, J. Morris, and C. Roman. (2011) <DOI:
10.1890/10-2037.1>.

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
