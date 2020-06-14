%global packname  RSuite
%global packver   0.37-253
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.37.253
Release:          2%{?dist}
Summary:          Supports Developing, Building and Deploying R Solution

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-logging 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-roxygen2 
BuildRequires:    R-CRAN-git2r 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-CRAN-httr 
Requires:         R-CRAN-logging 
Requires:         R-methods 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-roxygen2 
Requires:         R-CRAN-git2r 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-processx 
Requires:         R-CRAN-httr 

%description
Supports safe and reproducible solutions development in R. It will help
you with environment separation per project, dependency management, local
packages creation and preparing deployment packs for your solutions.

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
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/INDEX
