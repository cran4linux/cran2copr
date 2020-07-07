%global packname  isotree
%global packver   0.1.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.11
Release:          3%{?dist}
Summary:          Isolation-Based Outlier Detection

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-Rcereal 
Requires:         R-CRAN-Rcpp >= 1.0.1

%description
Fast and multi-threaded implementation of isolation forest (Liu, Ting,
Zhou (2008) <doi:10.1109/ICDM.2008.17>), extended isolation forest
(Hariri, Kind, Brunner (2018) <arXiv:1811.02141>), SCiForest (Liu, Ting,
Zhou (2010) <doi:10.1007/978-3-642-15883-4_18>), and fair-cut forest
(Cortes (2019) <arXiv:1911.06646>), for isolation-based outlier detection,
clustered outlier detection, distance or similarity approximation (Cortes
(2019) <arXiv:1910.12362>), and imputation of missing values (Cortes
(2019) <arXiv:1911.06646>), based on random or guided decision tree
splitting. Provides simple heuristics for fitting the model to categorical
columns and handling missing data, and offers options for varying between
random and guided splits, and for using different splitting criteria.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
