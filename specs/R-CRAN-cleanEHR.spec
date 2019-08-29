%global packname  cleanEHR
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          The Critical Care Clinical Data Processing Tools

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pander 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-pander 
Requires:         R-CRAN-knitr 

%description
An electronic health care record (EHR) data cleaning and processing
platform. It focus on heterogeneous high resolution longitudinal data. It
works with Critical Care Health Informatics Collaborative (CCHIC) dataset.
It is created to address various data reliability and accessibility
problems of EHRs as such.

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
%doc %{rlibdir}/%{packname}/conf
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/report
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
