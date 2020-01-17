%global packname  coreCT
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}
Summary:          Programmatic Analysis of Sediment Cores Using ComputedTomography Imaging

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
