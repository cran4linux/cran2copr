%global packname  DataExplorer
%global packver   0.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.1
Release:          3%{?dist}%{?buildtag}
Summary:          Automate Data Exploration and Treatment

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-rmarkdown >= 2.0
BuildRequires:    R-CRAN-reshape2 >= 1.4.3
BuildRequires:    R-CRAN-data.table >= 1.12.8
BuildRequires:    R-CRAN-scales >= 1.1.0
BuildRequires:    R-CRAN-networkD3 >= 0.4
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
BuildRequires:    R-parallel 
Requires:         R-CRAN-rmarkdown >= 2.0
Requires:         R-CRAN-reshape2 >= 1.4.3
Requires:         R-CRAN-data.table >= 1.12.8
Requires:         R-CRAN-scales >= 1.1.0
Requires:         R-CRAN-networkD3 >= 0.4
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-tools 
Requires:         R-parallel 

%description
Automated data exploration process for analytic tasks and predictive
modeling, so that users could focus on understanding data and extracting
insights. The package scans and analyzes each variable, and visualizes
them with typical graphical techniques. Common data processing methods are
also available to treat and format data.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/rmd_template
%{rlibdir}/%{packname}/INDEX
