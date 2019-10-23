%global packname  tacmagic
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Positron Emission Tomography Time-Activity Curve Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-R.matlab 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-pracma 
Requires:         R-utils 
Requires:         R-CRAN-R.matlab 

%description
To facilitate the analysis of positron emission tomography (PET) time
activity curve (TAC) data, and to encourage open science and
replicability, this package supports data loading and analysis of multiple
TAC file formats. Functions are available to analyze loaded TAC data for
individual participants or in batches. Major functionality includes
weighted TAC merging by region of interest (ROI), calculating models
including standardized uptake value ratio (SUVR) and distribution volume
ratio (DVR, Logan et al. 1996 <doi:10.1097/00004647-199609000-00008>),
basic plotting functions and calculation of cut-off values (Aizenstein et
al. 2008 <doi:10.1001/archneur.65.11.1509>). Please see the walkthrough
vignette for a detailed overview of 'tacmagic' functions.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
