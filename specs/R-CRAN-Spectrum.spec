%global packname  Spectrum
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Fast Adaptive Spectral Clustering for Single and Multi-View Data

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ClusterR 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-diptest 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ClusterR 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-diptest 

%description
A self-tuning spectral clustering method for single or multi-view data.
'Spectrum' uses a new type of adaptive density aware kernel that
strengthens connections in the graph based on common nearest neighbours.
It uses a tensor product graph data integration and diffusion procedure to
integrate different data sources and reduce noise. 'Spectrum' uses either
the eigengap or multimodality gap heuristics to determine the number of
clusters. The method is sufficiently flexible so that a wide range of
Gaussian and non-Gaussian structures can be clustered with automatic
selection of K.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
