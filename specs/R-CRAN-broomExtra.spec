%global packname  broomExtra
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}
Summary:          Enhancements for 'broom' Package Family

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-broom.mixed 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-parameters 
BuildRequires:    R-CRAN-performance 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-broom.mixed 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-parameters 
Requires:         R-CRAN-performance 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 

%description
Collection of functions to assist 'broom' and 'broom.mixed'
package-related data analysis workflows. In particular, the generic
functions tidy(), glance(), and augment() choose appropriate S3 methods
from these two packages depending on which package exports the needed
method. The 'grouped_' variants of the generics provides a convenient way
to execute functions across a combination of grouping variable(s) in a
dataframe. Additionally, tidy-and glance-like methods from 'parameters'
and 'performance' can also be accessed.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
