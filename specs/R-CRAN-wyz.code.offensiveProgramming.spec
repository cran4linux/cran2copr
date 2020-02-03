%global packname  wyz.code.offensiveProgramming
%global packver   1.1.17
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.17
Release:          1%{?dist}
Summary:          Wizardry Code Offensive Programming

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.4.0
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-data.table >= 1.11.8
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-crayon 
Requires:         R-CRAN-R6 >= 2.4.0
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-data.table >= 1.11.8
Requires:         R-methods 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-crayon 

%description
Allows to change R coding from defensive programming (i.e. many input
parameter checks implementation required) to offensive programming
(none/reduced number of parameter checks required). Provides code
instrumentation to ease this change. Should reduce the code size as many
controls and type checks have no more reason to exist. Should also speed
up processing as many checks will be reduced to single check.

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
%doc %{rlibdir}/%{packname}/code-samples
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
