%global packname  varTestnlme
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Variance Components Testing for Linear and Nonlinear MixedEffects Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-alabama 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-merDeriv 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-anocva 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-saemix 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-alabama 
Requires:         R-Matrix 
Requires:         R-CRAN-merDeriv 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-anocva 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-lme4 
Requires:         R-nlme 
Requires:         R-CRAN-saemix 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-foreach 
Requires:         R-methods 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 

%description
An implementation of the Likelihood ratio Test (LRT) for testing that, in
a (non)linear mixed effects model, the variances of a subset of the random
effects are equal to zero. There is no restriction on the subset of
variances that can be tested: for example, it is possible to test that all
the variances are equal to zero. Note that the implemented test is
asymptotic. This package should be used on model fits from packages
'nlme', 'lmer', and 'saemix'. Charlotte Baey, Paul-Henry Cournède and
Estelle Kuhn (2019) <doi:10.1016/j.csda.2019.01.014>.

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
