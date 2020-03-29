%global packname  PTXQC
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          Quality Report Generation for MaxQuant and mzTab Results

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2
BuildRequires:    R-CRAN-knitr >= 1.10
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggdendro 
BuildRequires:    R-grid 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-seqinr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-UpSetR 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-ggplot2 >= 2.2
Requires:         R-CRAN-knitr >= 1.10
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggdendro 
Requires:         R-grid 
Requires:         R-grDevices 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-kableExtra 
Requires:         R-methods 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-seqinr 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-UpSetR 
Requires:         R-CRAN-yaml 

%description
Generates Proteomics (PTX) quality control (QC) reports for shotgun LC-MS
data analyzed with the MaxQuant software suite (from .txt files) or mzTab
files (ideally from OpenMS 'QualityControl' tool). Reports are
customizable (target thresholds, subsetting) and available in HTML or PDF
format. Published in J. Proteome Res., Proteomics Quality Control: Quality
Control Software for MaxQuant Results (2015)
<doi:10.1021/acs.jproteome.5b00780>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/dragNdrop
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/reportTemplate
%{rlibdir}/%{packname}/INDEX
