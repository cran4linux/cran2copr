%global packname  GLMaSPU
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}%{?buildtag}
Summary:          An Adaptive Test on High Dimensional Parameters in GeneralizedLinear Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildRequires:    R-CRAN-mvtnorm >= 1.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.6
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-mvtnorm >= 1.0.0
Requires:         R-CRAN-Rcpp >= 0.12.6
Requires:         R-MASS 
Requires:         R-CRAN-mnormt 

%description
Several tests for high dimensional generalized linear models have been
proposed recently. In this package, we implemented a new test called
adaptive sum of powered score (aSPU) for high dimensional generalized
linear models, which is often more powerful than the existing methods in a
wide scenarios. We also implemented permutation based version of several
existing methods for research purpose. We recommend users use the aSPU
test for their real testing problem. You can learn more about the tests
implemented in the package via the following papers: 1. Pan, W., Kim, J.,
Zhang, Y., Shen, X. and Wei, P. (2014) <DOI:10.1534/genetics.114.165035> A
powerful and adaptive association test for rare variants, Genetics,
197(4). 2. Guo, B., and Chen, S. X. (2016) <DOI:10.1111/rssb.12152>. Tests
for high dimensional generalized linear models. Journal of the Royal
Statistical Society: Series B. 3. Goeman, J. J., Van Houwelingen, H. C.,
and Finos, L. (2011) <DOI:10.1093/biomet/asr016>. Testing against a
high-dimensional alternative in the generalized linear model: asymptotic
type I error control. Biometrika, 98(2).

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

%files
%{rlibdir}/%{packname}
