%global packname  imputeMulti
%global packver   0.6.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.4
Release:          3%{?dist}
Summary:          Imputation Methods for Multivariate Multinomial Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildRequires:    R-CRAN-gtools >= 3.3
BuildRequires:    R-CRAN-RSQLite >= 1.0
BuildRequires:    R-CRAN-DBI >= 0.4
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-gtools >= 3.3
Requires:         R-CRAN-RSQLite >= 1.0
Requires:         R-CRAN-DBI >= 0.4
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-Rcpp 

%description
Implements imputation methods using EM and Data Augmentation for
multinomial data following the work of Schafer 1997 <ISBN:
978-0-412-04061-0>.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
