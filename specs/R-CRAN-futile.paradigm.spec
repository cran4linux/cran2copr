%global packname  futile.paradigm
%global packver   2.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.4
Release:          3%{?dist}
Summary:          A framework for working in a functional programming paradigm inR

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-futile.options 
BuildRequires:    R-CRAN-RUnit 
Requires:         R-CRAN-futile.options 
Requires:         R-CRAN-RUnit 

%description
Provides dispatching implementations suitable for functional programming
paradigms. The framework provides a mechanism for attaching guards to
functions similar to Erlang, while also providing the safety of assertions
reminiscent of Eiffel.

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
%doc %{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/INDEX
