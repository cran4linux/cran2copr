%global packname  coopProductGame
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          3%{?dist}
Summary:          Cooperative Aspects of Linear Production Programming Problems

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.7.0
Requires:         R-core >= 2.7.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lpSolveAPI >= 5.5.2
BuildRequires:    R-CRAN-GameTheory >= 2.7
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-kappalab 
BuildRequires:    R-CRAN-gtools 
Requires:         R-CRAN-lpSolveAPI >= 5.5.2
Requires:         R-CRAN-GameTheory >= 2.7
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-grid 
Requires:         R-CRAN-kappalab 
Requires:         R-CRAN-gtools 

%description
Computes cooperative games and allocation rules associated with linear
production programming problems.

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
%{rlibdir}/%{packname}/INDEX
