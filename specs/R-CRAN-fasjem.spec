%global packname  fasjem
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          3%{?dist}
Summary:          A Fast and Scalable Joint Estimator for Learning MultipleRelated Sparse Gaussian Graphical Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-igraph 

%description
This is an R implementation of "A Fast and Scalable Joint Estimator for
Learning Multiple Related Sparse Gaussian Graphical Models" (FASJEM). The
FASJEM algorithm can be used to estimate multiple related precision
matrices. For instance, it can identify context-specific gene networks
from multi-context gene expression datasets. By performing data-driven
network inference from high-dimensional and heterogonous data sets, this
tool can help users effectively translate aggregated data into knowledge
that take the form of graphs among entities. Please run demo(fasjem) to
learn the basic functions provided by this package. For more details,
please see <http://proceedings.mlr.press/v54/wang17e/wang17e.pdf>.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
