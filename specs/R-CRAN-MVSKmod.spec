%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MVSKmod
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Matrix-Variate Skew Linear Regression Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Bessel 
BuildRequires:    R-CRAN-clusterGeneration 
BuildRequires:    R-CRAN-DistributionUtils 
BuildRequires:    R-CRAN-matlib 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-Bessel 
Requires:         R-CRAN-clusterGeneration 
Requires:         R-CRAN-DistributionUtils 
Requires:         R-CRAN-matlib 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-pracma 

%description
An implementation of the alternating expectation conditional maximization
(AECM) algorithm for matrix-variate variance gamma (MVVG) and
normal-inverse Gaussian (MVNIG) linear models. These models are designed
for settings of multivariate analysis with clustered non-uniform
observations and correlated responses. The package includes fitting and
prediction functions for both models, and an example dataset from a
periodontal on Gullah-speaking African Americans, with responses in
gaad_res, and covariates in gaad_cov. For more details on the
matrix-variate distributions used, see Gallaugher & McNicholas (2019)
<doi:10.1016/j.spl.2018.08.012>.

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
