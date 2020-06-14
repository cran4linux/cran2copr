%global packname  rtip
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          2%{?dist}
Summary:          Inequality, Welfare and Poverty Indices and Curves using theEU-SILC Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.1.0
BuildRequires:    R-CRAN-plyr >= 1.8.3
BuildRequires:    R-CRAN-rootSolve >= 1.7
BuildRequires:    R-boot >= 1.3
BuildRequires:    R-CRAN-mvtnorm >= 1.0
Requires:         R-CRAN-ggplot2 >= 2.1.0
Requires:         R-CRAN-plyr >= 1.8.3
Requires:         R-CRAN-rootSolve >= 1.7
Requires:         R-boot >= 1.3
Requires:         R-CRAN-mvtnorm >= 1.0

%description
R tools to measure and compare inequality, welfare and poverty using the
EU statistics on income and living conditions surveys.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
