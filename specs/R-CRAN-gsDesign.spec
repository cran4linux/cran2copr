%global packname  gsDesign
%global packver   3.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.1
Release:          2%{?dist}
Summary:          Group Sequential Design

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 >= 0.9.2
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 >= 0.9.2
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-rlang 
Requires:         R-methods 
Requires:         R-CRAN-xtable 
Requires:         R-graphics 
Requires:         R-CRAN-plyr 
Requires:         R-tools 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 

%description
Derives group sequential designs and describes their properties.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
