%global packname  OGI
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}
Summary:          Objective General Index

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lpSolve >= 5.6.13
BuildRequires:    R-stats >= 3.3.3
BuildRequires:    R-graphics >= 3.3.3
BuildRequires:    R-methods >= 3.3.3
Requires:         R-CRAN-lpSolve >= 5.6.13
Requires:         R-stats >= 3.3.3
Requires:         R-graphics >= 3.3.3
Requires:         R-methods >= 3.3.3

%description
Consider a data matrix of n individuals with p variates. The objective
general index (OGI) is a general index that combines the p variates into a
univariate index in order to rank the n individuals. The OGI is always
positively correlated with each of the variates. More details can be found
in Sei (2016) <doi:10.1016/j.jmva.2016.02.005>.

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
