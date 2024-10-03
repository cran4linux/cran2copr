%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PeakSegOptimal
%global packver   2024.10.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2024.10.1
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Segmentation Subject to Up-Down Constraints

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-penaltyLearning 
Requires:         R-CRAN-penaltyLearning 

%description
Computes optimal changepoint models using the Poisson likelihood for
non-negative count data, subject to the PeakSeg constraint: the first
change must be up, second change down, third change up, etc. For more info
about the models and algorithms, read "Constrained Dynamic Programming and
Supervised Penalty Learning Algorithms for Peak Detection"
<https://jmlr.org/papers/v21/18-843.html> by TD Hocking et al.

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
