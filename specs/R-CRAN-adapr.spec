%global packname  adapr
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}
Summary:          Implementation of an Accountable Data Analysis Process

License:          LGPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-git2r 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-versions 
BuildRequires:    R-CRAN-archivist 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-gdata 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-git2r 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-versions 
Requires:         R-CRAN-archivist 
Requires:         R-CRAN-doParallel 

%description
Tracks reading and writing within R scripts that are organized into a
directed acyclic graph. Contains an interactive shiny application
adaprApp(). Uses git2r package, Git and file hashes to track version
histories of input and output. See package vignette for how to get
started. V1.02 adds parallel execution of project scripts and function map
in vignette. Makes project specification argument last in order. V2.0 adds
project specific libraries, packrat option, and adaprSheet().

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
%doc %{rlibdir}/%{packname}/adapr_options.csv
%doc %{rlibdir}/%{packname}/adapr21
%doc %{rlibdir}/%{packname}/adaprTest.zip
%doc %{rlibdir}/%{packname}/cheatsheet_adapr.pdf
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
