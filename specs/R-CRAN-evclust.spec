%global packname  evclust
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Evidential Clustering

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-limSolve 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-limSolve 
Requires:         R-Matrix 

%description
Various clustering algorithms that produce a credal partition, i.e., a set
of Dempster-Shafer mass functions representing the membership of objects
to clusters. The mass functions quantify the cluster-membership
uncertainty of the objects. The algorithms are: Evidential c-Means (ECM),
Relational Evidential c-Means (RECM), Constrained Evidential c-Means
(CECM), EVCLUS and EK-NNclus.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
