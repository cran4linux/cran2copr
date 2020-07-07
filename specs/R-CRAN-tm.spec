%global packname  tm
%global packver   0.7-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.7
Release:          3%{?dist}
Summary:          Text Mining Package

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-NLP >= 0.2.0
BuildRequires:    R-CRAN-slam >= 0.1.37
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-NLP >= 0.2.0
Requires:         R-CRAN-slam >= 0.1.37
Requires:         R-CRAN-Rcpp 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-xml2 

%description
A framework for text mining applications within R.

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
%doc %{rlibdir}/%{packname}/ghostscript
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/stopwords
%doc %{rlibdir}/%{packname}/texts
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
