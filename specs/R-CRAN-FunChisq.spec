%global packname  FunChisq
%global packver   2.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          Model-Free Functional Chi-Squared and Exact Tests

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rdpack >= 0.6.1
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dqrng 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rdpack >= 0.6.1
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-CRAN-dqrng 

%description
Statistical hypothesis testing methods for inferring model-free functional
dependency using asymptotic chi-squared or exact distributions. Functional
test statistics are asymmetric and functionally optimal, unique from other
related statistics. Tests in this package reveal evidence for causality
based on the causality-by- functionality principle. They include
asymptotic functional chi-squared tests (Zhang & Song 2013)
<arXiv:1311.2707>, an adapted functional chi-squared test, and an exact
functional test (Zhong & Song 2019) <doi:10.1109/TCBB.2018.2809743>
(Nguyen et al. 2020) <doi:10.24963/ijcai.2020/372>. The normalized
functional chi-squared test was used by Best Performer 'NMSUSongLab' in
HPN-DREAM (DREAM8) Breast Cancer Network Inference Challenges (Hill et al.
2016) <doi:10.1038/nmeth.3773>. A function index (Zhong & Song 2019)
<doi:10.1186/s12920-019-0565-9> (Kumar et al. 2018)
<doi:10.1109/BIBM.2018.8621502> derived from the functional test statistic
offers a new effect size measure for the strength of functional
dependency, a better alternative to conditional entropy in many aspects.
For continuous data, these tests offer an advantage over regression
analysis when a parametric functional form cannot be assumed; for
categorical data, they provide a novel means to assess directional
dependency not possible with symmetrical Pearson's chi-squared or Fisher's
exact tests.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
