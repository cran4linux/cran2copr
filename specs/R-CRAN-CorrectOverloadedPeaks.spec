%global packname  CorrectOverloadedPeaks
%global packver   1.2.17
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.17
Release:          1%{?dist}
Summary:          Correct Overloaded Peaks from GC-APCI-MS Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-bitops 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-bitops 

%description
Analyzes and modifies metabolomics raw data (generated using GC-APCI-MS,
Gas Chromatography-Atmospheric Pressure Chemical Ionization-Mass
Spectrometry) to correct overloaded signals, i.e. ion intensities
exceeding detector saturation leading to a cut-off peak. Data in xcmsRaw
format are accepted as input and mzXML files can be processed
alternatively. Overloaded signals are detected automatically and modified
using an Gaussian or Isotopic-Ratio approach, QC plots are generated and
corrected data are stored within the original xcmsRaw or mzXML
respectively to allow further processing.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
