%global packname  RadOnc
%global packver   1.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.5
Release:          3%{?dist}%{?buildtag}
Summary:          Analytical Tools for Radiation Oncology

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-oro.dicom >= 0.5.0
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-ptinpoly 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-oro.dicom >= 0.5.0
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-ptinpoly 
Requires:         R-stats 
Requires:         R-utils 

%description
Designed for the import, analysis, and visualization of dosimetric and
volumetric data in Radiation Oncology, the tools herein enable import of
dose-volume histogram information from multiple treatment planning system
platforms and 3D structural representations and dosimetric information
from 'DICOM-RT' files.  These tools also enable subsequent visualization
and statistical analysis of these data.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
