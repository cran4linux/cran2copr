%global packname  shock
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Slope Heuristic for Block-Diagonal Covariance Selection in HighDimensional Gaussian Graphical Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-capushe 
BuildRequires:    R-CRAN-GGMselect 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-stats 
Requires:         R-CRAN-glasso 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-capushe 
Requires:         R-CRAN-GGMselect 
Requires:         R-CRAN-igraph 
Requires:         R-stats 

%description
Block-diagonal covariance selection for high dimensional Gaussian
graphical models. The selection procedure is based on the slope
heuristics.

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
%{rlibdir}/%{packname}/INDEX
