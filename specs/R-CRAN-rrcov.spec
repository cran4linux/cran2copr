%global packname  rrcov
%global packver   1.4-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.7
Release:          1%{?dist}
Summary:          Scalable Robust Estimators with High Breakdown Point

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-robustbase >= 0.92.1
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-lattice 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-pcaPP 
Requires:         R-CRAN-robustbase >= 0.92.1
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-stats4 
Requires:         R-CRAN-mvtnorm 
Requires:         R-lattice 
Requires:         R-cluster 
Requires:         R-CRAN-pcaPP 

%description
Robust Location and Scatter Estimation and Robust Multivariate Analysis
with High Breakdown Point.

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
%doc %{rlibdir}/%{packname}/bm
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
