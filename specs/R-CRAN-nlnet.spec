%global packname  nlnet
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Nonlinear Network Reconstruction, Clustering, and VariableSelection Based on DCOL (Distance Based on Conditional OrderedList)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-TSP 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-fdrtool 
BuildRequires:    R-CRAN-coin 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-earth 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-e1071 
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-TSP 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-fdrtool 
Requires:         R-CRAN-coin 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-earth 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-e1071 

%description
It includes four methods: DCOL-based K-profiles clustering, non-linear
network reconstruction, non-linear hierarchical clustering, and variable
selection for generalized additive model.

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
