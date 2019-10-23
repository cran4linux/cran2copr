%global packname  tadaatoolbox
%global packver   0.16.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.16.1
Release:          1%{?dist}
Summary:          Helpers for Data Analysis and Presentation Focused on UndergradPsychology

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-pixiedust 
BuildRequires:    R-CRAN-pwr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-car 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-pixiedust 
Requires:         R-CRAN-pwr 
Requires:         R-stats 
Requires:         R-CRAN-viridis 

%description
Contains functions for the easy display of statistical tests as well as
some convenience functions for data cleanup. It is meant to ease existing
workflows with packages like 'sjPlot', 'dplyr', and 'ggplot2'. The primary
components are the functions prefixed with 'tadaa_', which are built to
work in an interactive environment, but also print tidy markdown tables
powered by 'pixiedust' for the creation of 'RMarkdown' reports.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
