%global packname  archiDART
%global packver   3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3
Release:          3%{?dist}
Summary:          Plant Root System Architecture Analysis Using DART and RSMLFiles

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-TDA 
BuildRequires:    R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-gtools 
Requires:         R-grDevices 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-TDA 
Requires:         R-methods 

%description
Analysis of complex plant root system architectures (RSA) using the output
files created by Data Analysis of Root Tracings (DART), an open-access
software dedicated to the study of plant root architecture and development
across time series (Le Bot et al (2010) "DART: a software to analyse root
system architecture and development from captured images", Plant and Soil,
<DOI:10.1007/s11104-009-0005-2>), and RSA data encoded with the Root
System Markup Language (RSML) (Lobet et al (2015) "Root System Markup
Language: toward a unified root architecture description language", Plant
Physiology, <DOI:10.1104/pp.114.253625>). More information can be found in
Delory et al (2016) "archiDART: an R package for the automated computation
of plant root architectural traits", Plant and Soil,
<DOI:10.1007/s11104-015-2673-4>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
