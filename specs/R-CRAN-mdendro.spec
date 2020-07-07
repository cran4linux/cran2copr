%global packname  mdendro
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}
Summary:          Variable-Group Methods for Agglomerative Hierarchical Clustering

License:          LGPL-2.1
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rJava >= 0.9.8
Requires:         R-CRAN-rJava >= 0.9.8

%description
A collection of methods for agglomerative hierarchical clustering
strategies on a matrix of distances, implemented using the variable-group
approach introduced in Fernandez and Gomez (2008)
<doi:10.1007/s00357-008-9004-x>. Descriptive measures to analyze the
resulting hierarchical trees are also provided. In addition to the usual
clustering methods, two parameterized methods are provided to explore an
infinite family of hierarchical clustering strategies. When there are ties
in proximity values, the hierarchical trees obtained are unique and
independent of the order of the elements in the input matrix.

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
%doc %{rlibdir}/%{packname}/java
%{rlibdir}/%{packname}/INDEX
