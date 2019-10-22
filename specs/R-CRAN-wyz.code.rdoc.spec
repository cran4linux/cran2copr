%global packname  wyz.code.rdoc
%global packver   1.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.7
Release:          1%{?dist}
Summary:          Wizardry Code Offensive Programming R Documentation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.4.0
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-data.table >= 1.11.8
BuildRequires:    R-CRAN-wyz.code.offensiveProgramming >= 1.1.12
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-R6 >= 2.4.0
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-data.table >= 1.11.8
Requires:         R-CRAN-wyz.code.offensiveProgramming >= 1.1.12
Requires:         R-methods 
Requires:         R-CRAN-tidyr 

%description
Allows to generate automatically R documentation files from offensive
programming test cases. It populates most of the section of the
documentation content from the offensive programming instrumentation. This
reduces greatly the package producer effort and time to get to a fully
documented manual page for any instrumented function. Following
documentation sections are now automatically filled from instrumentation
data: title, description, usage, arguments, value, author, examples.
Sections references, notes and keyword are instrumented to industrialize
their production. Produced manual pages are ready for completion (e.g note
section if needed), language and phrasal adjustments. Main task for the
package producer is now review, no more content production.  Refer to
chapter 11 of Offensive Programming Book, Fabien GELINEAU (2019,
ISBN:979-10-699-4075-8), to learn about details and get value from this
package.

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
%doc %{rlibdir}/%{packname}/unit-testing
%{rlibdir}/%{packname}/INDEX
