%global packname  fastLink
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          2%{?dist}
Summary:          Fast Probabilistic Record Linkage with Missing Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.7
BuildRequires:    R-Matrix 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-FactoClass 
BuildRequires:    R-CRAN-adagio 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.12.7
Requires:         R-Matrix 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-FactoClass 
Requires:         R-CRAN-adagio 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-plotrix 
Requires:         R-grDevices 
Requires:         R-graphics 

%description
Implements a Fellegi-Sunter probabilistic record linkage model that allows
for missing data and the inclusion of auxiliary information. This includes
functionalities to conduct a merge of two datasets under the
Fellegi-Sunter model using the Expectation-Maximization algorithm. In
addition, tools for preparing, adjusting, and summarizing data merges are
included. The package implements methods described in Enamorado, Fifield,
and Imai (2019) ''Using a Probabilistic Model to Assist Merging of
Large-scale Administrative Records'', American Political Science Review
and is available at <http://imai.fas.harvard.edu/research/linkage.html>.

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
