%global packname  cabinets
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}
Summary:          Project Specific Workspace Organization Templates

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-here 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-git2r 
Requires:         R-CRAN-here 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-git2r 

%description
Creates project specific directory and file templates that are written to
a .Rprofile file. Upon starting a new R session, these templates can be
used to streamline the creation of new directories that are standardized
to the user's preferences.

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
%{rlibdir}/%{packname}/INDEX
