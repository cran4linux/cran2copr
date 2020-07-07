%global packname  diffman
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}
Summary:          Detect Differentiation Problems

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-dplyr 
Requires:         R-Matrix 
Requires:         R-CRAN-data.table 

%description
An algorithm based on graph theory tools to detect differentiation
problems. A differentiation problem occurs when aggregated data are
disseminated according to two different nomenclatures. By making the
difference for an additive variable X between an aggregate composed of
categories of the first nomenclature and an other aggregate, included in
that first aggregate, composed of categories of the second nomenclature,
it is sometimes possible to derive X on a small aggregate of records which
could then lead to a break of confidentiality. The purpose of this package
is to detect the set of aggregates composed of categories of the first
nomenclature which lead to a differentiation problem, when given a
confidentiality threshold. Reference: Vianney Costemalle (2019) <doi:
10.3233/SJI-190564>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/libs
