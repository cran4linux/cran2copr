%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dcce
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamic Common Correlated Effects Estimation for Panel Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-cli >= 3.0.0
BuildRequires:    R-CRAN-collapse >= 2.0.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-cli >= 3.0.0
Requires:         R-CRAN-collapse >= 2.0.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-tibble 

%description
Estimates heterogeneous coefficient models for large panels with
cross-sectional dependence. Implements the Mean Group (MG) estimator of
Pesaran and Smith (1995) <doi:10.1016/0304-4076(94)01644-F>, the Common
Correlated Effects (CCE) and Dynamic CCE (DCCE) estimators of Pesaran
(2006) <doi:10.1111/j.1468-0262.2006.00692.x> and Chudik and Pesaran
(2015) <doi:10.1016/j.jeconom.2015.03.007>, the regularized CCE of Juodis
(2022), the Augmented Mean Group (AMG) of Eberhardt and Teal (2010), the
Interactive Fixed Effects (IFE) estimator of Bai (2009)
<doi:10.3982/ECTA6135>, and long-run estimators including
Cross-Sectionally augmented Distributed Lag (CS-DL), Cross-Sectionally
augmented Autoregressive Distributed Lag (CS-ARDL), and Pooled Mean Group
(PMG) (Chudik et al. 2016; Shin et al. 1999). Also provides rolling-window
estimation, high-dimensional fixed effect absorption, spatial CCE via
user-supplied weight matrices, and structural break tests (Chow and
sup-Wald) following Andrews (1993), Bai and Perron (1998), and Ditzen,
Karavias and Westerlund (2024). Supplies a comprehensive cross-sectional
dependence (CD) test suite including the Pesaran (2015) CD test
<doi:10.1080/07474938.2014.956623>, the Juodis and Reese (2022) randomized
weighted CD (CDw) test, the Baltagi et al. (2012) bias-adjusted weighted
CD (CDw+) test, the Fan et al. (2015) Power Enhancement Approach (PEA)
test, and the Pesaran and Xie (2021) bias-corrected CD (CD*) test. Further
diagnostics include the Pesaran (2007) Cross-sectionally Augmented IPS
(CIPS) panel unit root test <doi:10.1002/jae.951>, the Westerlund (2007)
panel cointegration tests, the Dumitrescu and Hurlin (2012) panel Granger
causality test, the Im-Pesaran-Shin (IPS) and Levin-Lin-Chu (LLC) panel
unit root tests, the Pedroni (2004) and Kao (1999) residual cointegration
tests, the Swamy (1970) and Pesaran and Yamagata (2008) slope homogeneity
tests, a Hausman-type test for MG versus pooled, the exponent of
cross-sectional dependence from Bailey et al. (2016)
<doi:10.1002/jae.2490>, information criteria for Cross-Sectional Average
(CSA) selection, the rank condition classifier, impulse response
functions, cross-section and wild bootstrap inference, and
'broom'-compatible methods.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
