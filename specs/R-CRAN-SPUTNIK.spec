%global packname  SPUTNIK
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}
Summary:          SPatially aUTomatic deNoising for Ims toolKit

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-SDMTools 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-imager 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-infotheo 
BuildRequires:    R-parallel 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-spatstat 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-SDMTools 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-imager 
Requires:         R-methods 
Requires:         R-CRAN-infotheo 
Requires:         R-parallel 

%description
A set of tools for the peak filtering of mass spectrometry imaging data
(MSI or IMS) based on spatial distribution of signal. Given a
region-of-interest (ROI), representing the spatial region where the
informative signal is expected to be localized, a series of filters
determine which peak signals are characterized by an implausible spatial
distribution. The filters reduce the dataset dimensionality and increase
its information vs noise ratio, improving the quality of the unsupervised
analysis results, reducing data dimensionality and simplifying the
chemical interpretation.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
