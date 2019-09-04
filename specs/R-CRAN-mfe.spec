%global packname  mfe
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Meta-Feature Extractor

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-clusterCrit 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-infotheo 
BuildRequires:    R-MASS 
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-cluster 
Requires:         R-CRAN-clusterCrit 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-infotheo 
Requires:         R-MASS 
Requires:         R-rpart 
Requires:         R-CRAN-rrcov 
Requires:         R-stats 
Requires:         R-utils 

%description
Extracts meta-features from datasets to support the design of
recommendation systems based on Meta-Learning. The meta-features, also
called characterization measures, are able to characterize the complexity
of datasets and to provide estimates of algorithm performance. The package
contains not only the standard characterization measures, but also more
recent characterization measures. By making available a large set of
meta-feature extraction functions, tasks like comprehensive data
characterization, deep data exploration and large number of Meta-Learning
based data analysis can be performed. These concepts are described in the
paper: Adriano Rivolli, Luis Garcia, Carlos Soares, Joaquin Vanschoren,
and Andre de Carvalho. Towards Reproducible Empirical Research in
Meta-Learning.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
