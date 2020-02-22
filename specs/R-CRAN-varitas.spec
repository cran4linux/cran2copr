%global packname  varitas
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}
Summary:          Variant Calling in Targeted Analysis Sequencing Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-VennDiagram 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-VennDiagram 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-magrittr 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 

%description
Multi-caller variant analysis pipeline for targeted analysis sequencing
(TAS) data. Features a modular, automated workflow that can start with raw
reads and produces a user-friendly PDF summary and a spreadsheet
containing consensus variant information.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/ascii_logo.txt
%doc %{rlibdir}/%{packname}/config.yaml
%doc %{rlibdir}/%{packname}/ctdna_defaults.yaml
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/perl
%doc %{rlibdir}/%{packname}/report_template.Rmd
%doc %{rlibdir}/%{packname}/tumour_defaults.yaml
%{rlibdir}/%{packname}/INDEX
