%global __brp_check_rpaths %{nil}
%global packname  gitlabr
%global packver   1.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.6
Release:          3%{?dist}%{?buildtag}
Summary:          Access to the Gitlab API

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 1.1.0
BuildRequires:    R-CRAN-tibble >= 1.1
BuildRequires:    R-CRAN-dplyr >= 0.4.3
BuildRequires:    R-CRAN-purrr >= 0.2.2
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-arpr 
Requires:         R-CRAN-httr >= 1.1.0
Requires:         R-CRAN-tibble >= 1.1
Requires:         R-CRAN-dplyr >= 0.4.3
Requires:         R-CRAN-purrr >= 0.2.2
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-base64enc 
Requires:         R-utils 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-arpr 

%description
Provides R functions to access the API of the project and repository
management web application gitlab. For many common tasks (repository file
access, issue assignment and status, commenting) convenience wrappers are
provided, and in addition the full API can be used by specifying request
locations. Gitlab is open-source software and can be self-hosted or used
on gitlab.com.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/doc_save
%{rlibdir}/%{packname}/INDEX
