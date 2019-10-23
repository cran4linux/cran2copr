%global packname  CAM
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Causal Additive Model (CAM)

License:          FreeBSD
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-mboost 
BuildRequires:    R-Matrix 
BuildRequires:    R-parallel 
BuildRequires:    R-mgcv 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-mboost 
Requires:         R-Matrix 
Requires:         R-parallel 
Requires:         R-mgcv 

%description
The code takes an n x p data matrix and fits a Causal Additive Model (CAM)
for estimating the causal structure of the underlying process. The output
is a p x p adjacency matrix (a one in entry (i,j) indicates an edge from i
to j). Details of the algorithm can be found in: P. Bühlmann, J. Peters,
J. Ernest: "CAM: Causal Additive Models, high-dimensional order search and
penalized regression", Annals of Statistics 42:2526-2556, 2014.

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
