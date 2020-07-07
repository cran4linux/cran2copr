%global packname  Morpho
%global packver   2.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.8
Release:          3%{?dist}
Summary:          Calculations and Visualisations Related to GeometricMorphometrics

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-foreach >= 1.4.0
BuildRequires:    R-CRAN-doParallel >= 1.0.6
BuildRequires:    R-Matrix >= 1.0.1
BuildRequires:    R-CRAN-Rvcg >= 0.7
BuildRequires:    R-CRAN-RcppArmadillo >= 0.4
BuildRequires:    R-CRAN-rgl >= 0.100.18
BuildRequires:    R-MASS 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-colorRamps 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-foreach >= 1.4.0
Requires:         R-CRAN-doParallel >= 1.0.6
Requires:         R-Matrix >= 1.0.1
Requires:         R-CRAN-Rvcg >= 0.7
Requires:         R-CRAN-rgl >= 0.100.18
Requires:         R-MASS 
Requires:         R-parallel 
Requires:         R-CRAN-colorRamps 
Requires:         R-CRAN-Rcpp 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
A toolset for Geometric Morphometrics and mesh processing. This includes
(among other stuff) mesh deformations based on reference points,
permutation tests, detection of outliers, processing of sliding
semi-landmarks and semi-automated surface landmark placement.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
