%global packname  spreadr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Simulating Spreading Activation in a Network

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.5
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-extrafont 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-Rcpp >= 0.12.5
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-extrafont 
Requires:         R-CRAN-ggplot2 

%description
The notion of spreading activation is a prevalent metaphor in the
cognitive sciences. This package provides the tools for cognitive
scientists and psychologists to conduct computer simulations that
implement spreading activation in a network representation. The
algorithmic method implemented in 'spreadr' subroutines follows the
approach described in Vitevitch, Ercal, and Adagarla (2011, Frontiers),
who viewed activation as a fixed cognitive resource that could spread
among nodes that were connected to each other via edges or connections
(i.e., a network). See Vitevitch, M. S., Ercal, G., & Adagarla, B. (2011).
Simulating retrieval from a highly clustered network: Implications for
spoken word recognition. Frontiers in Psychology, 2, 369.
<doi:10.3389/fpsyg.2011.00369>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
