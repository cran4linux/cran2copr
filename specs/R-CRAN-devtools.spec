%global packname  devtools
%global packver   2.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.0
Release:          3%{?dist}
Summary:          Tools to Make Developing R Packages Easier

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-roxygen2 >= 7.1.0
BuildRequires:    R-CRAN-covr >= 3.5.0
BuildRequires:    R-CRAN-callr >= 3.4.3
BuildRequires:    R-CRAN-testthat >= 2.3.2
BuildRequires:    R-CRAN-withr >= 2.1.2
BuildRequires:    R-CRAN-remotes >= 2.1.1
BuildRequires:    R-CRAN-cli >= 2.0.2
BuildRequires:    R-CRAN-rversions >= 2.0.1
BuildRequires:    R-CRAN-jsonlite >= 1.6.1
BuildRequires:    R-CRAN-usethis >= 1.6.0
BuildRequires:    R-CRAN-httr >= 1.4.1
BuildRequires:    R-CRAN-glue >= 1.4.0
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-rcmdcheck >= 1.3.3
BuildRequires:    R-CRAN-desc >= 1.2.0
BuildRequires:    R-CRAN-sessioninfo >= 1.1.1
BuildRequires:    R-CRAN-memoise >= 1.1.0
BuildRequires:    R-CRAN-pkgbuild >= 1.0.6
BuildRequires:    R-CRAN-pkgload >= 1.0.2
BuildRequires:    R-CRAN-digest >= 0.6.25
BuildRequires:    R-CRAN-rlang >= 0.4.5
BuildRequires:    R-CRAN-ellipsis >= 0.3.0
BuildRequires:    R-CRAN-git2r >= 0.26.1
BuildRequires:    R-CRAN-DT >= 0.13
BuildRequires:    R-CRAN-rstudioapi >= 0.11
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-roxygen2 >= 7.1.0
Requires:         R-CRAN-covr >= 3.5.0
Requires:         R-CRAN-callr >= 3.4.3
Requires:         R-CRAN-testthat >= 2.3.2
Requires:         R-CRAN-withr >= 2.1.2
Requires:         R-CRAN-remotes >= 2.1.1
Requires:         R-CRAN-cli >= 2.0.2
Requires:         R-CRAN-rversions >= 2.0.1
Requires:         R-CRAN-jsonlite >= 1.6.1
Requires:         R-CRAN-usethis >= 1.6.0
Requires:         R-CRAN-httr >= 1.4.1
Requires:         R-CRAN-glue >= 1.4.0
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-rcmdcheck >= 1.3.3
Requires:         R-CRAN-desc >= 1.2.0
Requires:         R-CRAN-sessioninfo >= 1.1.1
Requires:         R-CRAN-memoise >= 1.1.0
Requires:         R-CRAN-pkgbuild >= 1.0.6
Requires:         R-CRAN-pkgload >= 1.0.2
Requires:         R-CRAN-digest >= 0.6.25
Requires:         R-CRAN-rlang >= 0.4.5
Requires:         R-CRAN-ellipsis >= 0.3.0
Requires:         R-CRAN-git2r >= 0.26.1
Requires:         R-CRAN-DT >= 0.13
Requires:         R-CRAN-rstudioapi >= 0.11
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Collection of package development tools.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
