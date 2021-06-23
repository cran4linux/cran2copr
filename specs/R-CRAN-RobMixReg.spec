%global __brp_check_rpaths %{nil}
%global packname  RobMixReg
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Mixture Regression

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-flexmix 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-robust 
BuildRequires:    R-CRAN-lars 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-glmnet 
Requires:         R-CRAN-flexmix 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-gtools 
Requires:         R-MASS 
Requires:         R-methods 
Requires:         R-CRAN-robust 
Requires:         R-CRAN-lars 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-gplots 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-stats 
Requires:         R-CRAN-glmnet 

%description
Finite mixture models are a popular technique for modelling unobserved
heterogeneity or to approximate general distribution functions in a
semi-parametric way. They are used in a lot of different areas such as
astronomy, biology, economics, marketing or medicine. This package is the
implementation of popular robust mixture regression methods based on
different algorithms including: fleximix, finite mixture models and latent
class regression; CTLERob, component-wise adaptive trimming likelihood
estimation; mixbi, bi-square estimation; mixL, Laplacian distribution;
mixt, t-distribution; TLE, trimmed likelihood estimation. The implemented
algorithms includes: CTLERob stands for Component-wise adaptive Trimming
Likelihood Estimation based mixture regression; mixbi stands for mixture
regression based on bi-square estimation; mixLstands for mixture
regression based on Laplacian distribution; TLE stands for Trimmed
Likelihood Estimation based mixture regression. For more detail of the
algorithms, please refer to below references. Reference: Chun Yu, Weixin
Yao, Kun Chen (2017) <doi:10.1002/cjs.11310>. NeyKov N, Filzmoser P,
Dimova R et al. (2007) <doi:10.1016/j.csda.2006.12.024>. Bai X, Yao W.
Boyer JE (2012) <doi:10.1016/j.csda.2012.01.016>. Wennan Chang, Xinyu
Zhou, Yong Zang, Chi Zhang, Sha Cao (2020) <arXiv:2005.11599>.

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
