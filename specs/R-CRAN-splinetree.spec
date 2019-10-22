%global packname  splinetree
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Longitudinal Regression Trees and Forests

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-rpart 
BuildRequires:    R-nlme 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-mosaic 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-treeClust 
BuildRequires:    R-CRAN-mclust 
Requires:         R-rpart 
Requires:         R-nlme 
Requires:         R-splines 
Requires:         R-CRAN-mosaic 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-treeClust 
Requires:         R-CRAN-mclust 

%description
Builds regression trees and random forests for longitudinal or functional
data using a spline projection method. Implements and extends the work of
Yu and Lambert (1999) <doi:10.1080/10618600.1999.10474847>. This method
allows trees and forests to be built while considering either level and
shape or only shape of response trajectories.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
