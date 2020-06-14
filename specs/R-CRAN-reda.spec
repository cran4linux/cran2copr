%global packname  reda
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          2%{?dist}
Summary:          Recurrent Event Data Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-splines2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-splines2 
Requires:         R-stats 

%description
Contains implementations of recurrent event data analysis routines
including (1) survival and recurrent event data simulation from stochastic
process point of view by the thinning method proposed by Lewis and Shedler
(1979) <doi:10.1002/nav.3800260304> and the inversion method introduced in
Cinlar (1975, ISBN:978-0486497976), (2) the mean cumulative function (MCF)
estimation by the Nelson-Aalen estimator of the cumulative hazard rate
function, (3) two-sample recurrent event responses comparison with the
pseudo-score tests proposed by Lawless and Nadeau (1995)
<doi:10.2307/1269617>, (4) gamma frailty model with spline rate function
following Fu, et al. (2016) <doi:10.1080/10543406.2014.992524>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/bib
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/tinytest
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
