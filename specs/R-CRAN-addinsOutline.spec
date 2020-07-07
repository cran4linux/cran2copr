%global packname  addinsOutline
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          3%{?dist}
Summary:          'RStudio' Addins for Show Outline of a R Markdown/'LaTeX'Project

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.7.7
BuildRequires:    R-CRAN-shinyFiles >= 0.7.2
BuildRequires:    R-CRAN-rstudioapi >= 0.5
BuildRequires:    R-CRAN-shiny >= 0.13
BuildRequires:    R-CRAN-miniUI >= 0.1
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-DT 
Requires:         R-CRAN-dplyr >= 0.7.7
Requires:         R-CRAN-shinyFiles >= 0.7.2
Requires:         R-CRAN-rstudioapi >= 0.5
Requires:         R-CRAN-shiny >= 0.13
Requires:         R-CRAN-miniUI >= 0.1
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-DT 

%description
'RStudio' allows to show and navigate for the outline of a R Markdown
file, but not for R Markdown projects with multiple files. For this
reason, I have developed several 'RStudio' addins capable of show project
outline. Each addin is specialized in showing projects of different types:
R Markdown project, 'bookdown' package project and 'LaTeX' project. There
is a configuration file that allows you to customize additional searches.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/rstudio
%doc %{rlibdir}/%{packname}/templates
%{rlibdir}/%{packname}/INDEX
