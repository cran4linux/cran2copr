%global packname  bigutilsr
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          3%{?dist}%{?buildtag}
Summary:          Utility Functions for Large-scale Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-bigparallelr >= 0.2.3
BuildRequires:    R-CRAN-bigassertr >= 0.1.1
BuildRequires:    R-CRAN-nabor 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-stats 
Requires:         R-CRAN-bigparallelr >= 0.2.3
Requires:         R-CRAN-bigassertr >= 0.1.1
Requires:         R-CRAN-nabor 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-RSpectra 
Requires:         R-stats 

%description
Utility functions for large-scale data. For now, package 'bigutilsr'
mainly includes functions for outlier detection and PCA projection.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/testdata
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
