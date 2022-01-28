%global __brp_check_rpaths %{nil}
%global packname  bibs
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Inference for the Birnbaum-Saunders Distribution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-GIGrvg 
Requires:         R-CRAN-GIGrvg 

%description
Developed for the following tasks. 1- Simulating and computing the maximum
likelihood estimator for the Birnbaum-Saunders (BS) distribution, 2-
Computing the Bayesian estimator for the parameters of the BS distribution
based on reference prior proposed by Xu and Tang (2010)
<doi:10.1016/j.csda.2009.08.004> and conjugate prior. 3- Computing the
Bayesian estimator for the BS distribution based on conjugate prior. 4-
Computing the Bayesian estimator for the BS distribution based on Jeffrey
prior given by Achcar (1993) <doi:10.1016/0167-9473(93)90170-X> 5-
Computing the Bayesian estimator for the BS distribution under progressive
type-II censoring scheme.

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
