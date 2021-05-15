%global packname  qcr
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Quality Control Review

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-qcc 
BuildRequires:    R-CRAN-fda.usc 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-qcc 
Requires:         R-CRAN-fda.usc 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-MASS 

%description
Univariate and multivariate SQC tools that completes and increases the SQC
techniques available in R. Apart from integrating different R packages
devoted to SQC ('qcc','MSQC'), provides nonparametric tools that are
highly useful when Gaussian assumption is not met. This package computes
standard univariate control charts for individual measurements, X-bar, S,
R, p, np, c, u, EWMA and CUSUM. In addition, it includes functions to
perform multivariate control charts such as Hotelling T2, MEWMA and
MCUSUM. As representative feature, multivariate nonparametric alternatives
based on data depth are implemented in this package: r, Q and S control
charts. In addition, Phase I and II control charts for functional data are
included. This package also allows the estimation of the most complete set
of capability indices from first to fourth generation, covering the
nonparametric alternatives, and performing the corresponding capability
analysis graphical outputs, including the process capability plots.

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
