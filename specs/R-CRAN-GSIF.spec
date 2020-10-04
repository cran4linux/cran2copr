%global packname  GSIF
%global packver   0.5-5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.5.1
Release:          3%{?dist}%{?buildtag}
Summary:          Global Soil Information Facilities

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sp >= 1.0.8
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RSAGA 
BuildRequires:    R-CRAN-dismo 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-aqp 
BuildRequires:    R-CRAN-plotKML 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-sp >= 1.0.8
Requires:         R-methods 
Requires:         R-CRAN-RSAGA 
Requires:         R-CRAN-dismo 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-aqp 
Requires:         R-CRAN-plotKML 
Requires:         R-CRAN-gstat 
Requires:         R-stats 
Requires:         R-CRAN-plyr 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-scales 

%description
Global Soil Information Facilities - tools (standards and functions) and
sample datasets for global soil mapping.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/USDA.csv
%doc %{rlibdir}/%{packname}/WRB.csv
%{rlibdir}/%{packname}/INDEX
