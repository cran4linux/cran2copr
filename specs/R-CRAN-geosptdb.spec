%global packname  geosptdb
%global packver   0.5-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          3%{?dist}
Summary:          Spatio-Temporal; Inverse Distance Weighting and Radial BasisFunctions with Distance-Based Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-CRAN-FD 
BuildRequires:    R-CRAN-StatMatch 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-minqa 
BuildRequires:    R-CRAN-limSolve 
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-CRAN-geospt 
Requires:         R-CRAN-FD 
Requires:         R-CRAN-StatMatch 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-minqa 
Requires:         R-CRAN-limSolve 
Requires:         R-CRAN-gsl 
Requires:         R-CRAN-geospt 

%description
Spatio-temporal: Inverse Distance Weighting (IDW) and radial basis
functions; optimization, prediction, summary statistics from leave-one-out
cross-validation, adjusting distance-based linear regression model and
generation of the principal coordinates of a new individual from Gower's
distance.

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
