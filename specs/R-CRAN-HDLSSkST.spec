%global packname  HDLSSkST
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Distribution-Free Exact High Dimensional Low Sample Sizek-Sample Tests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-stats 
Requires:         R-utils 

%description
We construct four new exact level (size) alpha tests for testing the
equality of k distributions, which can be conveniently used in high
dimensional low sample size setup based on clustering. These tests are
easy to implement and distribution-free. Under mild conditions, we have
proved the consistency of these tests as the dimension d of each
observation grows to infinity, whereas the sample size remains fixed. We
also apply step-down-procedure (1979) for multiple testing. Details are in
Biplab Paul, Shyamal K De and Anil K Ghosh (2020); Soham Sarkar and Anil K
Ghosh (2019) <doi:10.1109/TPAMI.2019.2912599>; William M Rand (1971)
<doi:10.1080/01621459.1971.10482356>; Cyrus R Mehta and Nitin R Patel
(1983) <doi:10.2307/2288652>; Joseph C Dunn (1973)
<doi:10.1080/01969727308546046>; Sture Holm (1979) <doi:10.2307/4615733>.

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
