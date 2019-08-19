%global packname  devtools
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}
Summary:          Tools to Make Developing R Packages Easier

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-roxygen2 >= 6.1.1
BuildRequires:    R-CRAN-testthat >= 2.1.1
BuildRequires:    R-CRAN-remotes >= 2.1.0
BuildRequires:    R-CRAN-usethis >= 1.5.0
BuildRequires:    R-CRAN-rcmdcheck >= 1.3.3
BuildRequires:    R-CRAN-sessioninfo >= 1.1.1
BuildRequires:    R-CRAN-pkgbuild >= 1.0.3
BuildRequires:    R-CRAN-pkgload >= 1.0.2
BuildRequires:    R-CRAN-memoise >= 1.0.0
BuildRequires:    R-CRAN-rstudioapi >= 0.7
BuildRequires:    R-CRAN-httr >= 0.4
BuildRequires:    R-CRAN-git2r >= 0.23.0
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-roxygen2 >= 6.1.1
Requires:         R-CRAN-testthat >= 2.1.1
Requires:         R-CRAN-remotes >= 2.1.0
Requires:         R-CRAN-usethis >= 1.5.0
Requires:         R-CRAN-rcmdcheck >= 1.3.3
Requires:         R-CRAN-sessioninfo >= 1.1.1
Requires:         R-CRAN-pkgbuild >= 1.0.3
Requires:         R-CRAN-pkgload >= 1.0.2
Requires:         R-CRAN-memoise >= 1.0.0
Requires:         R-CRAN-rstudioapi >= 0.7
Requires:         R-CRAN-httr >= 0.4
Requires:         R-CRAN-git2r >= 0.23.0
Requires:         R-CRAN-callr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-jsonlite 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-withr 

%description
Collection of package development tools.

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
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
