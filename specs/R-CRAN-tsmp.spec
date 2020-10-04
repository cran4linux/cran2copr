%global packname  tsmp
%global packver   0.4.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.14
Release:          3%{?dist}%{?buildtag}
Summary:          Time Series with Matrix Profile

License:          Apache License (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-CRAN-audio 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-RJSONIO 
Requires:         R-CRAN-RcppParallel >= 5.0.0
Requires:         R-CRAN-audio 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-doSNOW 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-magrittr 
Requires:         R-parallel 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-CRAN-RJSONIO 

%description
A toolkit implementing the Matrix Profile concept that was created by
CS-UCR <http://www.cs.ucr.edu/~eamonn/MatrixProfile.html>.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/API-v0.3.1
%doc %{rlibdir}/%{packname}/API-v0.3.2
%doc %{rlibdir}/%{packname}/API-v0.3.4
%doc %{rlibdir}/%{packname}/API-v0.3.5
%doc %{rlibdir}/%{packname}/API-v0.4.0
%doc %{rlibdir}/%{packname}/API-v0.4.10
%doc %{rlibdir}/%{packname}/API-v0.4.11
%doc %{rlibdir}/%{packname}/API-v0.4.12
%doc %{rlibdir}/%{packname}/API-v0.4.13
%doc %{rlibdir}/%{packname}/API-v0.4.14
%doc %{rlibdir}/%{packname}/API-v0.4.8
%doc %{rlibdir}/%{packname}/API-v0.4.9
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
