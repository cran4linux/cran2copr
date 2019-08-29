%global packname  erhcv
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}
Summary:          Equi-Rank Hierarchical Clustering Validation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-data.tree 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-stringi 
Requires:         R-utils 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-data.tree 

%description
Assesses the statistical significance of clusters for a given dataset
through bootstrapping and hypothesis testing of a given matrix of
empirical Spearman's rho, based on the technique of S. Gaiser et al.
(2010) <doi:10.1016/j.jmva.2010.07.008>.

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
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
