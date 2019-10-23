%global packname  funcy
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Functional Clustering Algorithms

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-flexclust 
BuildRequires:    R-splines 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-wavethresh 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-calibrate 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-sm 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-flexclust 
Requires:         R-splines 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-fda 
Requires:         R-methods 
Requires:         R-CRAN-wavethresh 
Requires:         R-CRAN-kernlab 
Requires:         R-parallel 
Requires:         R-CRAN-car 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-calibrate 
Requires:         R-cluster 
Requires:         R-CRAN-sm 
Requires:         R-CRAN-plyr 

%description
Unified framework to cluster functional data according to one of seven
models. All models are based on the projection of the curves onto a basis.
The main function funcit() calls wrapper functions for the existing
algorithms, so that input parameters are the same. A list is returned with
each entry representing the same or extended output for the corresponding
method. Method specific as well as general visualization tools are
available.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
