%global packname  LOGAN
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Log File Analysis in International Large-Scale Assessments

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-psych >= 1.7.8
BuildRequires:    R-foreign >= 0.8.69
BuildRequires:    R-CRAN-pander >= 0.6.1
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-modules 
Requires:         R-CRAN-psych >= 1.7.8
Requires:         R-foreign >= 0.8.69
Requires:         R-CRAN-pander >= 0.6.1
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-modules 

%description
Enables users to handle the dataset cleaning for conducting specific
analyses with the log files from two international educational
assessments: the Programme for International Student Assessment (PISA,
<http://www.oecd.org/pisa/>) and the Programme for the International
Assessment of Adult Competencies (PIAAC,
<http://www.oecd.org/skills/piaac/>). An illustration of the analyses can
be found on the LOGAN Shiny app
(<https://loganpackage.shinyapps.io/shiny/>) on your browser.

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
%doc %{rlibdir}/%{packname}/style.html
%{rlibdir}/%{packname}/INDEX
