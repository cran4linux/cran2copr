%global packname  RobMixReg
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
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
Requires:         R-CRAN-flexmix 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-gtools 
Requires:         R-MASS 
Requires:         R-methods 
Requires:         R-CRAN-robust 

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
Boyer JE (2012) <doi:10.1016/j.csda.2012.01.016>. Wennen Chang, Sha Cao,
Chi Zhang (2019) <doi:10.1101/426593>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
