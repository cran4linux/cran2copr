%global packname  messaging
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Conveniently Issue Messages, Warnings, and Errors

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr >= 1.3.0
BuildRequires:    R-CRAN-glue >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-rlang >= 0.2.0
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-stringr >= 1.3.0
Requires:         R-CRAN-glue >= 1.2.0
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-rlang >= 0.2.0
Requires:         R-CRAN-magrittr 

%description
Provides tools for creating and issuing nicely-formatted text within R
diagnostic messages and those messages given during warnings and errors.
The formatting of the messages can be customized using templating
features. Issues with singular and plural forms can be handled through
specialized syntax.

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
