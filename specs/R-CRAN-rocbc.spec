%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rocbc
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Inference for Box-Cox Based Receiver Operating Characteristic Curves

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-clinfun 
BuildRequires:    R-CRAN-splancs 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-clinfun 
Requires:         R-CRAN-splancs 
Requires:         R-CRAN-mvtnorm 

%description
Generation of Box-Cox based ROC curves and several aspects of inferences
and hypothesis testing. Can be used when inferences for one biomarker
(Bantis LE, Nakas CT, Reiser B. (2018) <doi:10.1002/bimj.201700107>) are
of interest or when comparisons of two correlated biomarkers (Bantis LE,
Nakas CT, Reiser B. (2021) <doi:10.1002/bimj.202000128>) are of interest.
Provides inferences and comparisons around the AUC, the Youden index, the
sensitivity at a given specificity level (and vice versa), the optimal
operating point of the ROC curve (in the Youden sense), and the Youden
based cutoff.

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
