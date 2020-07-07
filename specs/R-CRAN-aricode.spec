%global packname  aricode
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
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
et al (2009) <doi:10.1145/1553374.1553511>. Include AMI (Adjusted Mutual
Information) since version 0.1.2, a modified version of ARI (MARI) and
simple Chi-square distance since version 1.0.0.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
