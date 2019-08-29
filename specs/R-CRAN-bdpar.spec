%global packname  bdpar
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Big Data Preprocessing Architecture

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         python2
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ini 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-pipeR 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-svMisc 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-ini 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-pipeR 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-svMisc 
Requires:         R-tools 
Requires:         R-utils 

%description
Provide a tool to easily build customized data flows to pre-process large
volumes of information from different sources. To this end, 'bdpar' allows
to (i) easily use and create new functionalities and (ii) develop new data
source extractors according to the user needs. Additionally, the package
provides by default a predefined data flow to extract and pre-process the
most relevant information (tokens, dates, ... ) from some textual sources
(SMS, Email, tweets, YouTube comments).

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
%doc %{rlibdir}/%{packname}/exec
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/configurations
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/testFiles
%doc %{rlibdir}/%{packname}/testFiles_ExtractorSms
%doc %{rlibdir}/%{packname}/testFiles_InstanceFactory
%doc %{rlibdir}/%{packname}/testFiles_pipeline_execute_eml
%doc %{rlibdir}/%{packname}/testFiles_pipeline_execute_tsms
%doc %{rlibdir}/%{packname}/testResources
%{rlibdir}/%{packname}/INDEX
