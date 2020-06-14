%global packname  jmvconnect
%global packver   1.2.18
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.18
Release:          2%{?dist}
Summary:          Connect to the 'jamovi' Statistical Spreadsheet

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-jmvcore >= 1.2.19
BuildRequires:    R-CRAN-Rcpp >= 0.12.16
BuildRequires:    R-CRAN-evaluate 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-jmvcore >= 1.2.19
Requires:         R-CRAN-Rcpp >= 0.12.16
Requires:         R-CRAN-evaluate 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-httr 

%description
Methods to access data sets from the 'jamovi' statistical spreadsheet (see
<https://www.jamovi.org> for more information) from R.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
