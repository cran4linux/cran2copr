%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mixedsubjectsirt
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Item Response Theory Calibration with a Mixed Subjects Design

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mirt 
BuildRequires:    R-CRAN-rmutil 
Requires:         R-CRAN-mirt 
Requires:         R-CRAN-rmutil 

%description
Integrates large language model generated item responses into psychometric
calibration studies through a mixed-subjects design for unidimensional
two-parameter and one-parameter logistic item response theory models.
Human pilot responses are augmented with model-generated responses using a
prediction-powered inference estimator (Angelopoulos, Bates, Fannjiang,
Jordan and Zrnic (2023) <doi:10.1126/science.adi6000>; Angelopoulos, Duchi
and Zrnic (2023) <doi:10.48550/arXiv.2311.01453>) adapted to marginal
maximum-likelihood estimation, following the mixed-subjects design of
Broska, Howes and van Loon (2025) <doi:10.1177/00491241251326865>. The
estimator is anchored to the human responses and is asymptotically
unbiased for the human item parameters at any tuning weight; the weight on
the synthetic responses is chosen to minimize propagated ability-score
risk, down-weighting uninformative or biased generated responses.
Louis-corrected sandwich standard errors, ability scoring, cross-fitted
tuning, and scale linking are also provided.

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
