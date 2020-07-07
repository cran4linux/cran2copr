%global packname  acc
%global packver   1.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.3
Release:          3%{?dist}
Summary:          Exploring Accelerometer Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-mhsmm 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-PhysicalActivity 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-circlize 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-mhsmm 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-PhysicalActivity 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-plyr 
Requires:         R-methods 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-circlize 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-Rcpp 

%description
Processes accelerometer data from uni-axial and tri-axial devices, and
generates data summaries. Also includes functions to plot, analyze, and
simulate accelerometer data.

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
