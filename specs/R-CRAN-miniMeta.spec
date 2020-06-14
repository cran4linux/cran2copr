%global packname  miniMeta
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          2%{?dist}
Summary:          Web Application to Run Meta-Analyses

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-meta 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-rhandsontable 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-WriteXLS 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-meta 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-rhandsontable 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-WriteXLS 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-jsonlite 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-stats 

%description
Shiny web application to run meta-analyses. Essentially a graphical
front-end to package 'meta' for R. Can be useful as an educational tool,
and for quickly analyzing and sharing meta-analyses. Provides output to
quickly fill in GRADE (Grading of Recommendations, Assessment, Development
and Evaluations) Summary-of-Findings tables. Importantly, it allows
further processing of the results inside R, in case more specific analyses
are needed.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
