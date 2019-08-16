%global packname  RUnit
%global packver   0.4.32
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.32
Release:          1%{?dist}
Summary:          R Unit Test Framework

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 2.5.0
Requires:         R-core >= 2.5.0
BuildArch:        noarch
BuildRequires:    R-utils >= 2.5.0
BuildRequires:    R-methods >= 2.5.0
BuildRequires:    R-graphics >= 2.5.0
Requires:         R-utils >= 2.5.0
Requires:         R-methods >= 2.5.0
Requires:         R-graphics >= 2.5.0

%description
R functions implementing a standard Unit Testing framework, with
additional code inspection and report generation tools.

%prep
%setup -q -c -n %{packname}
sed -i '/Sexpr/d' %{packname}/man/checkFuncs.Rd
 sed -i 's/"runitVirtualClassTest.r")}/"runitVirtualClassTest.r"/g' %{packname}/man/checkFuncs.Rd

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/share
%doc %{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/INDEX
