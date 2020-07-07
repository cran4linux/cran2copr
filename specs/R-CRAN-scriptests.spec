%global packname  scriptests
%global packver   1.0-16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.16
Release:          3%{?dist}
Summary:          Transcript-Based Unit Tests that are Easy to Create and Maintain

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
Requires:         R-methods 

%description
Support for using .Rt (transcript) tests in the tests directory of a
package.  Provides more convenience and features than the standard
.R/.Rout.save tests.  Tests can be run under R CMD check and also
interactively.  Provides source.pkg() for quickly loading code, DLLs, and
data from a package for use in an edit/compile/test development cycle.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/sccversion.txt
%doc %{rlibdir}/%{packname}/svnversion.txt
%{rlibdir}/%{packname}/INDEX
