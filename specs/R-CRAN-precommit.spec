%global packname  precommit
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Pre-Commit Hooks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-usethis >= 1.6.0
BuildRequires:    R-CRAN-docopt 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-here 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-R.cache 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rprojroot 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-usethis >= 1.6.0
Requires:         R-CRAN-docopt 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-here 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-R.cache 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rprojroot 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-yaml 

%description
Useful git hooks for R building on top of the multi-language framework
'pre-commit' for hook management. This package provides git hooks for
common tasks like formatting files with 'styler' or spell checking as well
as wrapper functions to access the 'pre-commit' executable.

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
%{rlibdir}/%{packname}/bin
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/pre-commit-config-pkg.yaml
%doc %{rlibdir}/%{packname}/pre-commit-config-proj.yaml
%doc %{rlibdir}/%{packname}/pre-commit-hooks.yaml
%doc %{rlibdir}/%{packname}/spell-check-exclude-to-config
%doc %{rlibdir}/%{packname}/usethis-legacy-hook
%{rlibdir}/%{packname}/INDEX
