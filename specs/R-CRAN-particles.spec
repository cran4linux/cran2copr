%global packname  particles
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          3%{?dist}
Summary:          A Graph Based Particle Simulator Based on D3-Force

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-tidygraph 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-tidygraph 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-igraph 
Requires:         R-stats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-Rcpp 
Requires:         R-mgcv 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-dplyr 

%description
Simulating particle movement in 2D space has many application. The
'particles' package implements a particle simulator based on the ideas
behind the 'd3-force' 'JavaScript' library. 'particles' implements all
forces defined in 'd3-force' as well as others such as vector fields,
traps, and attractors.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
