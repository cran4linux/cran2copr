%global packname  outsider.base
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Base Package for 'Outsider'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-utils >= 3.1
BuildRequires:    R-CRAN-callr >= 3.0.0
BuildRequires:    R-CRAN-sys >= 2.1
BuildRequires:    R-CRAN-yaml >= 2.0
BuildRequires:    R-CRAN-withr >= 2.0
BuildRequires:    R-CRAN-devtools >= 1.1
BuildRequires:    R-CRAN-jsonlite >= 1.1
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-praise 
Requires:         R-utils >= 3.1
Requires:         R-CRAN-callr >= 3.0.0
Requires:         R-CRAN-sys >= 2.1
Requires:         R-CRAN-yaml >= 2.0
Requires:         R-CRAN-withr >= 2.0
Requires:         R-CRAN-devtools >= 1.1
Requires:         R-CRAN-jsonlite >= 1.1
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-praise 

%description
Base package for 'outsider' <https://github.com/ropensci/outsider>. The
'outsider' package and its sister packages enable the installation and
running of external, command-line software within R. This base package is
a key dependency of the user-facing 'outsider' package as it provides the
utilities for interfacing between 'Docker' <https://www.docker.com> and R.
It is intended that end-users of 'outsider' do not directly work with this
base package.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
