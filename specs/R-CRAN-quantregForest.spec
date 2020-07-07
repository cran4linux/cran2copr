%global packname  quantregForest
%global packver   1.3-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.7
Release:          3%{?dist}
Summary:          Quantile Regression Forests

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-stats 
Requires:         R-parallel 

%description
Quantile Regression Forests is a tree-based ensemble method for estimation
of conditional quantiles. It is particularly well suited for
high-dimensional data. Predictor variables of mixed classes can be
handled. The package is dependent on the package 'randomForest', written
by Andy Liaw.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
