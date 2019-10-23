%global packname  DatabionicSwarm
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Swarm Intelligence for Self-Organized Clustering

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-CRAN-GeneralizedUmatrix 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-deldir 
Requires:         R-CRAN-GeneralizedUmatrix 

%description
Algorithms implementing populations of agents that interact with one
another and sense their environment may exhibit emergent behavior such as
self-organization and swarm intelligence. Here, a swarm system called
databionic swarm (DBS) is introduced. DBS is able to adapt itself to
structures of high-dimensional data such as natural clusters characterized
by distance and/or density based structures in the data space. The first
module is the parameter-free projection method called Pswarm (Pswarm()),
which exploits the concepts of self-organization and emergence, game
theory, swarm intelligence and symmetry considerations. The second module
is the parameter-free high-dimensional data visualization technique, which
generates projected points on the topographic map with hypsometric tints
defined by the generalized U-matrix (GeneratePswarmVisualization()). The
third module is the clustering method itself with non-critical parameters
(DBSclustering()). Clustering can be verified by the visualization and
vice versa. The term DBS refers to the method as a whole. It enables even
a non-professional in the field of data mining to apply its algorithms for
visualization and/or clustering to data sets with completely different
structures drawn from diverse research fields. The package is based on the
book of Thrun, M.C.: "Projection Based Clustering through
Self-Organization and Swarm Intelligence" (2018)
<DOI:10.1007/978-3-658-20540-9>. A comparison to 26 common clustering
algorithms on 15 datasets is presented on the website.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
