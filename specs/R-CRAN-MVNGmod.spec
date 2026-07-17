%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MVNGmod
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Matrix-Variate Non-Gaussian Linear Regression Models

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
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-Bessel 
Requires:         R-CRAN-clusterGeneration 
Requires:         R-CRAN-DistributionUtils 
Requires:         R-CRAN-matlib 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-purrr 

%description
Fits matrix-variate variance-gamma (MVVG) and matrix-variate
normal-inverse-Gaussian (MVNIG) linear regression models using
expectation-conditional maximization (ECM) algorithms. The models
accommodate clustered matrix-valued responses, with unequal numbers of
observations across subjects, correlated responses, skewness, and
within-subject dependence. Functions are provided for model fitting,
prediction, and subject-level influence assessment using approximate
generalized Cook's distances. The package also includes motivating
periodontal data from Gullah-speaking African Americans with Type-II
diabetes. For details on the underlying matrix-variate distributions (MVVG
and MVNIG), see Gallaugher and McNicholas (2019,
<doi:10.1016/j.spl.2018.08.012>).

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
