%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  agghoo
%global packver   0.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Aggregated Hold-Out Cross Validation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-class 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-FNN 
Requires:         R-CRAN-class 
Requires:         R-parallel 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-FNN 

%description
The 'agghoo' procedure is an alternative to usual cross-validation.
Instead of choosing the best model trained on V subsamples, it determines
a winner model for each subsample, and then aggregates the V outputs. For
the details, see "Aggregated hold-out" by Guillaume Maillard, Sylvain
Arlot, Matthieu Lerasle (2021) <arXiv:1909.04890> published in Journal of
Machine Learning Research 22(20):1--55.

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
