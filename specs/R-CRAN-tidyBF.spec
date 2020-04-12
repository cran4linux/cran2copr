%global packname  tidyBF
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Tidy Wrapper for 'BayesFactor' Package

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-BayesFactor 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ipmisc 
BuildRequires:    R-CRAN-metaBMA 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-BayesFactor 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ipmisc 
Requires:         R-CRAN-metaBMA 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 

%description
Provides helper functions that make it easy to run 'BayesFactor' package
tests on a data which is in a tidy format. Additionally, it provides a
more consistent syntax and by default returns a dataframe with rich
details. These functions can also return expressions containing results
from Bayes Factor tests that can then be displayed on custom plots.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
