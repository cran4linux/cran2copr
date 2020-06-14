%global packname  nodeHarvest
%global packver   0.7-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.3
Release:          2%{?dist}
Summary:          Node Harvest for Regression and Classification

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-randomForest 
Requires:         R-graphics 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-randomForest 

%description
Node harvest is a simple interpretable tree-like estimator for
high-dimensional regression and classification. A few nodes are selected
from an initially large ensemble of nodes, each associated with a positive
weight. New observations can fall into one or several nodes and
predictions are the weighted average response across all these groups. The
package offers visualization of the estimator. Predictions can return the
nodes a new observation fell into, along with the mean response of
training observations in each node, offering a simple explanation of the
prediction.

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
