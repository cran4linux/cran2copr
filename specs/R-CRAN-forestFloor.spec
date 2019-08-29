%global packname  forestFloor
%global packver   1.11.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.11.1
Release:          1%{?dist}
Summary:          Visualizes Random Forests with Feature Contributions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    mesa-libGL-devel
BuildRequires:    mesa-libGLU-devel
BuildRequires:    zlib-devel
Requires:         mesa-libGL
Requires:         mesa-libGLU
Requires:         zlib
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.3
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-kknn 
BuildRequires:    R-CRAN-randomForest 
Requires:         R-CRAN-Rcpp >= 0.11.3
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-kknn 
Requires:         R-CRAN-randomForest 

%description
Form visualizations of high dimensional mapping structures of random
forests and feature contributions.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
