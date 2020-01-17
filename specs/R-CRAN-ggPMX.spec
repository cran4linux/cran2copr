%global packname  ggPMX
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          'ggplot2' Based Tool to Facilitate Diagnostic Plots for NLMEModels

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rmarkdown 

%description
At Novartis, we aimed at standardizing the set of diagnostic plots used
for modeling activities in order to reduce the overall effort required for
generating such plots. For this, we developed a guidance that proposes an
adequate set of diagnostics and a toolbox, called 'ggPMX' to execute them.
'ggPMX' is a toolbox that can generate all diagnostic plots at a quality
sufficient for publication and submissions using few lines of code.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/extra
%doc %{rlibdir}/%{packname}/init
%doc %{rlibdir}/%{packname}/rmarkdown
%doc %{rlibdir}/%{packname}/templates
%{rlibdir}/%{packname}/testdata
%{rlibdir}/%{packname}/INDEX
