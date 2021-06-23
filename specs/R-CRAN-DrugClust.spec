%global __brp_check_rpaths %{nil}
%global packname  DrugClust
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Implementation of a Machine Learning Framework for PredictingDrugs Side Effects

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-MESS 
BuildRequires:    R-CRAN-cclust 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-utils 
BuildRequires:    R-base 
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-MESS 
Requires:         R-CRAN-cclust 
Requires:         R-cluster 
Requires:         R-CRAN-e1071 
Requires:         R-utils 
Requires:         R-base 

%description
An implementation of a Machine Learning Framework for prediction of new
drugs Side Effects. Firstly drugs are clustered with respect to their
features description and secondly predictions are made, according to
Bayesian scores. Moreover it can perform protein enrichment considering
the proteins clustered together in the first step of the algorithm. This
last tool is of extreme interest for biologist and drug discovery
purposes, given the fact that it can be used either as a validation of the
clusters obtained, as well as for the possible discovery of new
interactions between certain side effects and non targeted pathways.
Clustering of the drugs in the feature space can be done using K-Means,
PAM or K-Seeds (a novel clustering algorithm proposed by the author).

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
