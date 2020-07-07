%global packname  RmixmodCombi
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Combining Mixture Components for Clustering

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-Rmixmod >= 2.0.1
BuildRequires:    R-CRAN-Rcpp >= 0.8.0
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
Requires:         R-CRAN-Rmixmod >= 2.0.1
Requires:         R-CRAN-Rcpp >= 0.8.0
Requires:         R-methods 
Requires:         R-graphics 

%description
The Rmixmod package provides model-based clustering by fitting a mixture
model (e.g. Gaussian components for quantitative continuous data) to the
data and identifying each cluster with one of its components. The number
of components can be determined from the data, typically using the BIC
criterion. In practice, however, individual clusters can be poorly fitted
by Gaussian distributions, and in that case model-based clustering tends
to represent one non-Gaussian cluster by a mixture of two or more Gaussian
components. If the number of mixture components is interpreted as the
number of clusters, this can lead to overestimation of the number of
clusters. This is because BIC selects the number of mixture components
needed to provide a good approximation to the density. This package,
RmixmodCombi, according to emph{Combining Mixture Components for
Clustering} by J.P. Baudry, A.E. Raftery, G. Celeux, K. Lo, R. Gottardo,
combines the components of the EM/BIC solution (provided by Rmixmod)
hierarchically according to an entropy criterion. This yields a clustering
for each number of clusters less than or equal to K. These clusterings can
be compared on substantive grounds, and we also provide a way of selecting
the number of clusters via a piecewise linear regression fit to the
(possibly rescaled) entropy plot.

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
