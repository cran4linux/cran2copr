%global packname  rEMM
%global packver   1.0-11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.11
Release:          1%{?dist}
Summary:          Extensible Markov Model for Modelling Temporal RelationshipsBetween Clusters

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-CRAN-proxy >= 0.4.7
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-clusterGeneration 
BuildRequires:    R-MASS 
BuildRequires:    R-utils 
Requires:         R-CRAN-proxy >= 0.4.7
Requires:         R-CRAN-igraph 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-cluster 
Requires:         R-CRAN-clusterGeneration 
Requires:         R-MASS 
Requires:         R-utils 

%description
Implements TRACDS (Temporal Relationships between Clusters for Data
Streams), a generalization of Extensible Markov Model (EMM). TRACDS adds a
temporal or order model to data stream clustering by superimposing a
dynamically adapting Markov Chain. Also provides an implementation of EMM
(TRACDS on top of tNN data stream clustering). Development of this package
was supported in part by NSF IIS-0948893 and R21HG005912 from the National
Human Genome Research Institute.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
