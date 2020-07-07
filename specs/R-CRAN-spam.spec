%global packname  spam
%global packver   2.5-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5.1
Release:          3%{?dist}
Summary:          SPArse Matrix

License:          LGPL-2 | BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-dotCall64 
BuildRequires:    R-grid 
BuildRequires:    R-methods 
Requires:         R-CRAN-dotCall64 
Requires:         R-grid 
Requires:         R-methods 

%description
Set of functions for sparse matrix algebra. Differences with other sparse
matrix packages are: (1) we only support (essentially) one sparse matrix
format, (2) based on transparent and simple structure(s), (3) tailored for
MCMC calculations within G(M)RF. (4) and it is fast and scalable (with the
extension package spam64). Documentation about 'spam' is provided by
vignettes included in this package, see also Furrer and Sain (2010)
<doi:10.18637/jss.v036.i10>; see 'citation("spam")' for details.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%license %{rlibdir}/%{packname}/0LICENSE
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/demodata
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
