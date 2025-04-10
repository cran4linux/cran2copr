%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mlr3resampling
%global packver   2025.3.30
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2025.3.30
Release:          1%{?dist}%{?buildtag}
Summary:          Resampling Algorithms for 'mlr3' Framework

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mlr3 >= 0.21.1
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-paradox 
BuildRequires:    R-CRAN-mlr3misc 
Requires:         R-CRAN-mlr3 >= 0.21.1
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-paradox 
Requires:         R-CRAN-mlr3misc 

%description
A supervised learning algorithm inputs a train set, and outputs a
prediction function, which can be used on a test set. If each data point
belongs to a subset (such as geographic region, year, etc), then how do we
know if subsets are similar enough so that we can get accurate predictions
on one subset, after training on Other subsets? And how do we know if
training on All subsets would improve prediction accuracy, relative to
training on the Same subset? SOAK, Same/Other/All K-fold cross-validation,
<doi:10.48550/arXiv.2410.08643> can be used to answer these question, by
fixing a test subset, training models on Same/Other/All subsets, and then
comparing test error rates (Same versus Other and Same versus All). Also
provides code for estimating how many train samples are required to get
accurate predictions on a test set.

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
