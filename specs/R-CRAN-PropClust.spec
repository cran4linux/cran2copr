%global __brp_check_rpaths %{nil}
%global packname  PropClust
%global packver   1.4-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.6
Release:          3%{?dist}%{?buildtag}
Summary:          Propensity Clustering and Decomposition

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-fastcluster 
BuildRequires:    R-CRAN-dynamicTreeCut 
BuildRequires:    R-stats 
Requires:         R-CRAN-fastcluster 
Requires:         R-CRAN-dynamicTreeCut 
Requires:         R-stats 

%description
Implementation of propensity clustering and decomposition as described in
Ranola et al. (2013) <doi:10.1186/1752-0509-7-21>. Propensity
decomposition can be viewed on the one hand as a generalization of the
eigenvector-based approximation of correlation networks, and on the other
hand as a generalization of random multigraph models and conformity-based
decompositions.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
