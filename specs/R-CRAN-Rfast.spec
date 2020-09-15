%global packname  Rfast
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Collection of Efficient and Extremely Fast R Functions

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-CRAN-RcppZiggurat 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.3
Requires:         R-CRAN-RcppZiggurat 

%description
A collection of fast (utility) functions for data analysis. Column- and
row- wise means, medians, variances, minimums, maximums, many t, F and
G-square tests, many regressions (normal, logistic, Poisson), are some of
the many fast functions. References: a) Tsagris M., Papadakis M. (2018).
Taking R to its limits: 70+ tips. PeerJ Preprints 6:e26605v1
<doi:10.7287/peerj.preprints.26605v1>. b) Tsagris M. and Papadakis M.
(2018). Forward regression in R: from the extreme slow to the extreme
fast. Journal of Data Science, 16(4): 771--780.
<doi:10.6339/JDS.201810_16(4).00006>.

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
