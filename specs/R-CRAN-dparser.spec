%global packname  dparser
%global packver   0.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          3%{?dist}%{?buildtag}
Summary:          Port of 'Dparser' Package

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-methods 
Requires:         R-CRAN-digest 
Requires:         R-methods 

%description
A Scannerless GLR parser/parser generator.  Note that GLR standing for
"generalized LR", where L stands for "left-to-right" and R stands for
"rightmost (derivation)".  For more information see
<https://en.wikipedia.org/wiki/GLR_parser>. This parser is based on the
Tomita (1987) algorithm. (Paper can be found at
<http://acl-arc.comp.nus.edu.sg/archives/acl-arc-090501d3/data/pdf/anthology-PDF/J/J87/J87-1004.pdf>).
The original 'dparser' package documentation can be found at
<http://dparser.sourceforge.net/>.  This allows you to add mini-languages
to R (like RxODE's ODE mini-language Wang, Hallow, and James 2015
<DOI:10.1002/psp4.12052>) or to parse other languages like 'NONMEM' to
automatically translate them to R code.  To use this in your code, add a
LinkingTo dparser in your DESCRIPTION file and instead of using #include
<dparse.h> use #include <dparser.h>.  This also provides a R-based port of
the make_dparser <http://dparser.sourceforge.net/d/make_dparser.cat>
command called mkdparser().  Additionally you can parse an arbitrary
grammar within R using the dparse() function, which works on most OSes and
is mainly for grammar testing.  The fastest parsing, of course, occurs at
the C level, and is suggested.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/ansic.test.g
%doc %{rlibdir}/%{packname}/tran.g
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/include
