%global __brp_check_rpaths %{nil}
%global packname  knitLatex
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          3%{?dist}%{?buildtag}
Summary:          'Knitr' Helpers - Mostly Tables

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-knitr >= 1.10.5
Requires:         R-CRAN-knitr >= 1.10.5

%description
Provides several helper functions for working with 'knitr' and 'LaTeX'. It
includes 'xTab' for creating traditional 'LaTeX' tables, 'lTab' for
generating 'longtable' environments, and 'sTab' for generating a
'supertabular' environment. Additionally, this package contains a
knitr_setup() function which fixes a well-known bug in 'knitr', which
distorts the 'results="asis"' command when used in conjunction with
user-defined commands; and a com command (<<com=TRUE>>=) which renders the
output from 'knitr' as a 'LaTeX' command.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
