%global packname  magic
%global packver   1.5-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.9
Release:          2%{?dist}
Summary:          Create and Investigate Magic Squares

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-abind 
Requires:         R-CRAN-abind 

%description
A collection of efficient, vectorized algorithms for the creation and
investigation of magic squares and hypercubes, including a variety of
functions for the manipulation and analysis of arbitrarily dimensioned
arrays.  The package includes methods for creating normal magic squares of
any order greater than 2.  The ultimate intention is for the package to be
a computerized embodiment all magic square knowledge, including direct
numerical verification of properties of magic squares (such as recent
results on the determinant of odd-ordered semimagic squares).  Some
antimagic functionality is included.  The package also serves as a
rebuttal to the often-heard comment "I thought R was just for statistics".

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
