%global packname  usethis
%global packver   1.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.1
Release:          1%{?dist}
Summary:          Automate Package and Project Setup

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 2.7
BuildRequires:    R-CRAN-fs >= 1.3.0
BuildRequires:    R-CRAN-glue >= 1.3.0
BuildRequires:    R-CRAN-rprojroot >= 1.2
BuildRequires:    R-CRAN-gh >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 0.4.3
BuildRequires:    R-CRAN-clipr >= 0.3.0
BuildRequires:    R-CRAN-git2r >= 0.23
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-desc 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rematch2 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-whisker 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-curl >= 2.7
Requires:         R-CRAN-fs >= 1.3.0
Requires:         R-CRAN-glue >= 1.3.0
Requires:         R-CRAN-rprojroot >= 1.2
Requires:         R-CRAN-gh >= 1.1.0
Requires:         R-CRAN-rlang >= 0.4.3
Requires:         R-CRAN-clipr >= 0.3.0
Requires:         R-CRAN-git2r >= 0.23
Requires:         R-CRAN-cli 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-desc 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rematch2 
Requires:         R-CRAN-rstudioapi 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-whisker 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-yaml 

%description
Automate package and project setup tasks that are otherwise performed
manually. This includes setting up unit testing, test coverage, continuous
integration, Git, 'GitHub', licenses, 'Rcpp', 'RStudio' projects, and
more.

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
%doc %{rlibdir}/%{packname}/templates
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
