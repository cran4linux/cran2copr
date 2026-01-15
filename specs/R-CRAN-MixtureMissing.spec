%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MixtureMissing
%global packver   3.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Robust and Flexible Model-Based Clustering for Data Sets with Missing Values at Random

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-numDeriv >= 8.1.1
BuildRequires:    R-CRAN-MASS >= 7.3
BuildRequires:    R-CRAN-mclust >= 5.0.0
BuildRequires:    R-CRAN-mice >= 3.10.0
BuildRequires:    R-CRAN-cluster >= 2.1.2
BuildRequires:    R-CRAN-mnormt >= 2.0.2
BuildRequires:    R-CRAN-mvtnorm >= 1.1.2
BuildRequires:    R-CRAN-Bessel >= 0.6.0
Requires:         R-CRAN-numDeriv >= 8.1.1
Requires:         R-CRAN-MASS >= 7.3
Requires:         R-CRAN-mclust >= 5.0.0
Requires:         R-CRAN-mice >= 3.10.0
Requires:         R-CRAN-cluster >= 2.1.2
Requires:         R-CRAN-mnormt >= 2.0.2
Requires:         R-CRAN-mvtnorm >= 1.1.2
Requires:         R-CRAN-Bessel >= 0.6.0

%description
Implementations of various robust and flexible model-based clustering
methods for data sets with missing values at random (Tong and Tortora,
2025, <doi:10.18637/jss.v115.i03>). Two main models are: Multivariate
Contaminated Normal Mixture (MCNM, Tong and Tortora, 2022,
<doi:10.1007/s11634-021-00476-1>) and Multivariate Generalized Hyperbolic
Mixture (MGHM, Wei et al., 2019, <doi:10.1016/j.csda.2018.08.016>).
Mixtures via some special or limiting cases of the multivariate
generalized hyperbolic distribution are also included: Normal-Inverse
Gaussian, Symmetric Normal-Inverse Gaussian, Skew-Cauchy, Cauchy, Skew-t,
Student's t, Normal, Symmetric Generalized Hyperbolic, Hyperbolic
Univariate Marginals, Hyperbolic, and Symmetric Hyperbolic. Funding: This
work was partially supported by the National Science foundation NSF Grant
NO. 2209974.

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
