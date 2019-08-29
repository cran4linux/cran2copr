%global packname  libsoc
%global packver   0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7
Release:          1%{?dist}
Summary:          Read, Create and Write 'PharmML' Standard Output (so) XML Files

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    libxml2-devel
Requires:         libxml2
BuildRequires:    R-devel >= 2.14.1
Requires:         R-core >= 2.14.1
BuildRequires:    R-methods 
Requires:         R-methods 

%description
Handle 'PharmML' (Pharmacometrics Markup Language) standard output (SO)
XML files. SO files can be created, read, manipulated and written through
a data binding from the XML structure to a tree structure of R objects.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/licenses
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
