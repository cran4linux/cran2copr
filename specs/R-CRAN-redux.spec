%global packname  redux
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          R Bindings to 'hiredis'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    hiredis
BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-storr >= 1.1.1
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-storr >= 1.1.1
Requires:         R-CRAN-R6 

%description
A 'hiredis' wrapper that includes support for transactions, pipelining,
blocking subscription, serialisation of all keys and values, 'Redis' error
handling with R errors. Includes an automatically generated 'R6' interface
to the full 'hiredis' 'API'.  Generated functions are faithful to the
'hiredis' documentation while attempting to match R's argument semantics.
Serialisation must be explicitly done by the user, but both binary and
text-mode serialisation is supported.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/COPYING.hiredis
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
