%global packname  sensitivity2x2xk
%global packver   1.01
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.01
Release:          3%{?dist}%{?buildtag}
Summary:          Sensitivity Analysis for 2x2xk Tables in Observational Studies

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-BiasedUrn 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-stats 
Requires:         R-CRAN-BiasedUrn 
Requires:         R-CRAN-mvtnorm 

%description
Performs exact or approximate adaptive or nonadaptive
Cochran-Mantel-Haenszel-Birch tests and sensitivity analyses for one or
two 2x2xk tables in observational studies.

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
