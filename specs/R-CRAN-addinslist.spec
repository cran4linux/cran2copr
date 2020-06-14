%global packname  addinslist
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          2%{?dist}
Summary:          Discover and Install Useful RStudio Addins

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shinyjs >= 0.6
BuildRequires:    R-CRAN-rappdirs >= 0.3.1
BuildRequires:    R-CRAN-rvest >= 0.3.1
BuildRequires:    R-CRAN-shiny >= 0.13.2
BuildRequires:    R-CRAN-xml2 >= 0.1.2
BuildRequires:    R-CRAN-DT >= 0.1
BuildRequires:    R-CRAN-miniUI >= 0.1
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-remotes 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-utils 
Requires:         R-CRAN-shinyjs >= 0.6
Requires:         R-CRAN-rappdirs >= 0.3.1
Requires:         R-CRAN-rvest >= 0.3.1
Requires:         R-CRAN-shiny >= 0.13.2
Requires:         R-CRAN-xml2 >= 0.1.2
Requires:         R-CRAN-DT >= 0.1
Requires:         R-CRAN-miniUI >= 0.1
Requires:         R-CRAN-curl 
Requires:         R-CRAN-remotes 
Requires:         R-CRAN-rmarkdown 
Requires:         R-utils 

%description
Browse through a continuously updated list of existing RStudio addins and
install/uninstall their corresponding packages.

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
%doc %{rlibdir}/%{packname}/gadgets
%doc %{rlibdir}/%{packname}/media
%doc %{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/INDEX
