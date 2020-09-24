%global packname  EquiSurv
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Modeling, Confidence Intervals and Equivalence of Survival Curves

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-eha 
BuildRequires:    R-graphics 
Requires:         R-survival 
Requires:         R-CRAN-eha 
Requires:         R-graphics 

%description
We provide a non-parametric and a parametric approach to investigate the
equivalence (or non-inferiority) of two survival curves, obtained from two
given datasets. The test is based on the creation of confidence intervals
at pre-specified time points. For the non-parametric approach, the curves
are given by Kaplan-Meier curves and the variance for calculating the
confidence intervals is obtained by Greenwood's formula. The parametric
approach is based on estimating the underlying distribution, where the
user can choose between a Weibull, Exponential, Gaussian, Logistic,
Log-normal or a Log-logistic distribution. Estimates for the variance for
calculating the confidence bands are obtained by a (parametric) bootstrap
approach. For this bootstrap censoring is assumed to be exponentially
distributed and estimates are obtained from the datasets under
consideration. All details can be found in K.Moellenhoff and A.Tresch:
Survival analysis under non-proportional hazards: investigating
non-inferiority or equivalence in time-to-event data <arXiv:2009.06699>.

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
