%global packname  lfl
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          2%{?dist}
Summary:          Linguistic Fuzzy Logic

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-forecast >= 5.5
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-forecast >= 5.5
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-zoo 

%description
Various algorithms related to linguistic fuzzy logic: mining for
linguistic fuzzy association rules, composition of fuzzy relations,
performing perception-based logical deduction (PbLD), and forecasting
time-series using fuzzy rule-based ensemble (FRBE).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
