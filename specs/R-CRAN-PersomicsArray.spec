%global packname  PersomicsArray
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Automated Persomics Array Image Extraction

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-tiff 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-grDevices 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-tiff 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-raster 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-stats 

%description
Automated identification of printed array positions from high content
microscopy images and the export of those positions as individual images
written to output as multi-layered tiff files.

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
