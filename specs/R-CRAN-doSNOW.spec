%global packname  doSNOW
%global packver   1.0.18
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.18
Release:          3%{?dist}%{?buildtag}
Summary:          Foreach Parallel Adaptor for the 'snow' Package

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.5.0
Requires:         R-core >= 2.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-foreach >= 1.2.0
BuildRequires:    R-CRAN-iterators >= 1.0.0
BuildRequires:    R-CRAN-snow >= 0.3.0
BuildRequires:    R-utils 
Requires:         R-CRAN-foreach >= 1.2.0
Requires:         R-CRAN-iterators >= 1.0.0
Requires:         R-CRAN-snow >= 0.3.0
Requires:         R-utils 

%description
Provides a parallel backend for the %dopar% function using the snow
package of Tierney, Rossini, Li, and Sevcikova.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/INDEX
