%global packname  ISRaD
%global packver   1.5.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.6
Release:          1%{?dist}%{?buildtag}
Summary:          Tools and Data for the International Soil Radiocarbon Database

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyr >= 1.0
BuildRequires:    R-CRAN-dplyr >= 0.8
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-maps 
Requires:         R-CRAN-tidyr >= 1.0
Requires:         R-CRAN-dplyr >= 0.8
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-writexl 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-maps 

%description
This is the central location for data and tools for the development,
maintenance, analysis, and deployment of the International Soil
Radiocarbon Database (ISRaD). ISRaD was developed as a collaboration
between the U.S. Geological Survey Powell Center and the Max Planck
Institute for Biogeochemistry. This R package provides tools for accessing
and manipulating ISRaD data, compiling local data using the ISRaD data
structure, and simple query and reporting functions for ISRaD. For more
detailed information visit the ISRaD website at:
<https://soilradiocarbon.org/>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
