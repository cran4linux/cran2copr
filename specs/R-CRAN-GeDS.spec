%global packname  GeDS
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Geometrically Designed Spline Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.1
BuildRequires:    R-splines 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rmpfr 
Requires:         R-CRAN-Rcpp >= 0.12.1
Requires:         R-splines 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-Rmpfr 

%description
Geometrically Designed Spline ('GeDS') Regression is a non-parametric
geometrically motivated method for fitting variable knots spline predictor
models in one or two independent variables, in the context of generalized
(non-)linear models. 'GeDS' estimates the number and position of the knots
and the order of the spline, assuming the response variable has a
distribution from the exponential family. A description of the method can
be found in Kaishev et al. (2016) <doi:10.1007/s00180-015-0621-7> and
Dimitrova et al. (2017) <https://openaccess.city.ac.uk/18460>.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
