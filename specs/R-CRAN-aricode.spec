%global packname  aricode
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          2%{?dist}
Summary:          Efficient Computations of Standard Clustering ComparisonMeasures

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-Matrix 
Requires:         R-CRAN-Rcpp 

%description
Implements an efficient O(n) algorithm based on bucket-sorting for fast
computation of standard clustering comparison measures. Available measures
include adjusted Rand index (ARI), normalized information distance (NID),
normalized mutual information (NMI), adjusted mutual information (AMI),
normalized variation information (NVI) and entropy, as described in Vinh
et al (2009) <doi:10.1145/1553374.1553511>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/check_speed.R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
