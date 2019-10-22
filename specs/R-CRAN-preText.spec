%global packname  preText
%global packver   0.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.2
Release:          1%{?dist}
Summary:          Diagnostics to Assess the Effects of Text PreprocessingDecisions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-quanteda 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-grid 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-topicmodels 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-ecodist 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-quanteda 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-vegan 
Requires:         R-grid 
Requires:         R-parallel 
Requires:         R-CRAN-topicmodels 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-ecodist 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-reshape2 

%description
Functions to assess the effects of different text preprocessing decisions
on the inferences drawn from the resulting document-term matrices they
generate.

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
