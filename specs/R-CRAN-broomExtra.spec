%global packname  broomExtra
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Enhancements for 'broom' Package Family

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-broom >= 0.5.3
BuildRequires:    R-CRAN-rlang >= 0.4.2
BuildRequires:    R-CRAN-broom.mixed >= 0.2.4
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-broom >= 0.5.3
Requires:         R-CRAN-rlang >= 0.4.2
Requires:         R-CRAN-broom.mixed >= 0.2.4

%description
Collection of functions to assist 'broom' and 'broom.mixed'
package-related data analysis workflows. In particular, the generic
functions tidy(), glance(), and augment() choose appropriate S3 methods
from these two packages depending on which package exports the needed
method. Additionally, 'grouped_' variants of the generics provides a
convenient way to execute functions across a combination of grouping
variable(s) in a dataframe.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
