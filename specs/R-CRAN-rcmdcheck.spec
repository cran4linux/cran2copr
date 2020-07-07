%global packname  rcmdcheck
%global packver   1.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.3
Release:          3%{?dist}
Summary:          Run 'R CMD check' from 'R' and Capture Results

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-callr >= 3.1.1.9000
BuildRequires:    R-CRAN-desc >= 1.2.0
BuildRequires:    R-CRAN-sessioninfo >= 1.1.1
BuildRequires:    R-CRAN-cli >= 1.1.0
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-pkgbuild 
BuildRequires:    R-CRAN-prettyunits 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rprojroot 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-xopen 
Requires:         R-CRAN-callr >= 3.1.1.9000
Requires:         R-CRAN-desc >= 1.2.0
Requires:         R-CRAN-sessioninfo >= 1.1.1
Requires:         R-CRAN-cli >= 1.1.0
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-pkgbuild 
Requires:         R-CRAN-prettyunits 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rprojroot 
Requires:         R-utils 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-xopen 

%description
Run 'R CMD check' from 'R' and capture the results of the individual
checks. Supports running checks in the background, timeouts, pretty
printing and comparing check results.

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
