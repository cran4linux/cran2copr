%global packname  purrrogress
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          2%{?dist}
Summary:          Add Progress Bars to Mapping Functions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-hms 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pkgcond 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-testextra 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-hms 
Requires:         R-methods 
Requires:         R-CRAN-pkgcond 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-testextra 
Requires:         R-utils 
Requires:         R-CRAN-rlang 

%description
Provides functions to easily add progress bars to apply calls.

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
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
