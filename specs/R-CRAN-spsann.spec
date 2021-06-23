%global __brp_check_rpaths %{nil}
%global packname  spsann
%global packver   2.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Optimization of Sample Configurations using Spatial SimulatedAnnealing

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pedometrics 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-SpatialTools 
Requires:         R-methods 
Requires:         R-CRAN-pedometrics 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-SpatialTools 

%description
Methods to optimize sample configurations using spatial simulated
annealing. Multiple objective functions are implemented for various
purposes, such as variogram estimation, spatial trend estimation and
spatial interpolation. A general purpose spatial simulated annealing
function enables the user to define his/her own objective function.
Solutions for augmenting existing sample configurations and solving
multi-objective optimization problems are available as well.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
