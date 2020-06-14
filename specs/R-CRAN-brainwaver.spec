%global packname  brainwaver
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          2%{?dist}
Summary:          Basic wavelet analysis of multivariate time series with avisualisation and parametrisation using graph theory.

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.10.0
Requires:         R-core >= 1.10.0
BuildRequires:    R-CRAN-waveslim 
Requires:         R-CRAN-waveslim 

%description
This package computes the correlation matrix for each scale of a wavelet
decomposition, namely the one performed by the R package waveslim
(Whitcher, 2000). An hypothesis test is applied to each entry of one
matrix in order to construct an adjacency matrix of a graph. The graph
obtained is finally analysed using the small-world theory (Watts and
Strogatz, 1998) and using the computation of efficiency (Latora, 2001),
tested using simulated attacks. The brainwaver project is complementary to
the camba project for brain-data preprocessing. A collection of scripts
(with a makefile) is avalaible to download along with the brainwaver
package, see information on the webpage mentioned below.

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
%{rlibdir}/%{packname}/libs
