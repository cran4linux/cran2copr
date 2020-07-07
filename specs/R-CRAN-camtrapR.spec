%global packname  camtrapR
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          3%{?dist}
Summary:          Camera Trap Data Management and Preparation of Occupancy andSpatial Capture-Recapture Analyses

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         perl(Image::ExifTool)
BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-overlap 
BuildRequires:    R-CRAN-secr 
BuildRequires:    R-CRAN-data.table 
Requires:         R-methods 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-overlap 
Requires:         R-CRAN-secr 
Requires:         R-CRAN-data.table 

%description
Management of and data extraction from camera trap data in wildlife
studies. The package provides a workflow for storing and sorting camera
trap photos (and videos), tabulates records of species and individuals,
and creates detection/non-detection matrices for occupancy and spatial
capture-recapture analyses with great flexibility. In addition, it can
visualise species activity data and provides simple mapping functions with
GIS export.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/pictures
%{rlibdir}/%{packname}/INDEX
