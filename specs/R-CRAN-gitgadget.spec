%global packname  gitgadget
%global packver   0.4.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.4
Release:          1%{?dist}
Summary:          Rstudio Addin for Version Control and Assignment Managementusing Git

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 3.2
BuildRequires:    R-CRAN-callr >= 2.0.4
BuildRequires:    R-CRAN-usethis >= 1.5.1
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-shiny >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-shinyFiles >= 0.7.3
BuildRequires:    R-CRAN-rstudioapi >= 0.7
BuildRequires:    R-CRAN-miniUI >= 0.1.1.1
BuildRequires:    R-CRAN-markdown 
Requires:         R-CRAN-curl >= 3.2
Requires:         R-CRAN-callr >= 2.0.4
Requires:         R-CRAN-usethis >= 1.5.1
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-shiny >= 1.1.0
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-shinyFiles >= 0.7.3
Requires:         R-CRAN-rstudioapi >= 0.7
Requires:         R-CRAN-miniUI >= 0.1.1.1
Requires:         R-CRAN-markdown 

%description
An Rstudio addin for version control that allows users to clone
repositories, create and delete branches, and sync forks on GitHub,
GitLab, etc. Furthermore, the addin uses the GitLab API to allow
instructors to create forks and merge requests for all students/teams with
one click of a button.

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
%doc %{rlibdir}/%{packname}/app
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/INDEX
