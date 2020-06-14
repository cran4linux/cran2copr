%global packname  tmod
%global packver   0.40
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.40
Release:          2%{?dist}
Summary:          Feature Set Enrichment Analysis for Metabolomics andTranscriptomics

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-beeswarm 
BuildRequires:    R-CRAN-tagcloud 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plotwidgets 
Requires:         R-CRAN-beeswarm 
Requires:         R-CRAN-tagcloud 
Requires:         R-CRAN-XML 
Requires:         R-methods 
Requires:         R-CRAN-plotwidgets 

%description
Methods and feature set definitions for feature or gene set enrichment
analysis in transcriptional and metabolic profiling data. Package includes
tests for enrichment based on ranked lists of features, functions for
visualisation and multivariate functional analysis.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/tmod_user_manual.pdf
%{rlibdir}/%{packname}/INDEX
