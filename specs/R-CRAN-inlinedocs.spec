%global packname  inlinedocs
%global packver   2019.12.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2019.12.5
Release:          1%{?dist}
Summary:          Convert Inline Comments to Documentation

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.9
Requires:         R-core >= 2.9
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-methods 
Requires:         R-utils 

%description
Generates Rd files from R source code with comments. The main features of
the default syntax are that (1) docs are defined in comments near the
relevant code, (2) function argument names are not repeated in comments,
and (3) examples are defined in R code, not comments. It is also easy to
define a new syntax.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/silly
%doc %{rlibdir}/%{packname}/testfiles
%{rlibdir}/%{packname}/INDEX
