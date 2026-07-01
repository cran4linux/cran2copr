%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AIDA
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Interval DAta

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-cellWise 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-fmsb 
BuildRequires:    R-CRAN-ggbeeswarm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-kde1d 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
Requires:         R-CRAN-cellWise 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-fmsb 
Requires:         R-CRAN-ggbeeswarm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-kde1d 
Requires:         R-CRAN-MASS 
Requires:         R-methods 

%description
Tools for the analysis of interval-valued data, including construction,
visualization, and statistical modeling. The package provides the
'intData' class for representing interval-valued data, along with
functions to aggregate microdata and to estimate parameters of latent
distributions. Barycenter and covariance matrix estimation is implemented
based on the Mallows distance (Oliveira et al. (2025)
<doi:10.48550/arXiv.2407.05105>). Robust estimation of the symbolic
covariance matrix is implemented via the Interval Minimum Covariance
Determinant (IMCD) estimator, enabling outlier detection based on the
robust squared Interval-Mahalanobis distance, as proposed by Loureiro et
al. (2026b) <doi:10.48550/arXiv.2604.26769>. Explainable outlier detection
is supported through Shapley value based decomposition of the squared
robust Interval-Mahalanobis distance, allowing assessment of variable
contributions to outlyingness (Loureiro et al. (2026a)
<doi:10.48550/arXiv.2606.26307>). Shapley interaction indices are also
implemented, along with visualization tools to support interpretation of
the results.

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
