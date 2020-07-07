%global packname  Demerelate
%global packver   0.9-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.3
Release:          3%{?dist}
Summary:          Functions to Calculate Relatedness on Diploid Genetic Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-fts 
BuildRequires:    R-CRAN-sfsmisc 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-mlogit 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-fts 
Requires:         R-CRAN-sfsmisc 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-mlogit 

%description
Functions to calculate pairwise relatedness on diploid genetic datasets.
Different estimators for relatedness can be combined with information on
geographical distances. Information on heterozygosity, allele- and
genotype diversity as well as genetic F-statistics are provided for each
population.

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
