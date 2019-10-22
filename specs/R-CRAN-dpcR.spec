%global packname  dpcR
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          1%{?dist}
Summary:          Digital PCR Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-binom 
BuildRequires:    R-CRAN-chipPCR 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-dgof 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-qpcR 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-rateratio.test 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-spatstat 
Requires:         R-methods 
Requires:         R-CRAN-binom 
Requires:         R-CRAN-chipPCR 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-evd 
Requires:         R-CRAN-dgof 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-qpcR 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-rateratio.test 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-spatstat 

%description
Analysis, visualisation and simulation of digital polymerase chain
reaction (dPCR) (Burdukiewicz et al. (2016)
<doi:10.1016/j.bdq.2016.06.004>). Supports data formats of commercial
systems (Bio-Rad QX100 and QX200; Fluidigm BioMark) and other systems.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/dpcr_density_gui
%doc %{rlibdir}/%{packname}/dpcReport
%doc %{rlibdir}/%{packname}/test_counts_gui
%{rlibdir}/%{packname}/INDEX
