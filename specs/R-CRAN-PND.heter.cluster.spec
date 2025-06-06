%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PND.heter.cluster
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating the Cluster Specific Treatment Effects in Partially Nested Designs

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-SuperLearner 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-origami 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-glue 
Requires:         R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-SuperLearner 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-origami 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-glue 

%description
Implements the methods for assessing heterogeneous cluster-specific
treatment effects in partially nested designs as described in Liu (2024)
<doi:10.1037/met0000723>. The estimation uses the multiply robust method,
allowing for the use of machine learning methods in model estimation
(e.g., random forest, neural network, and the super learner ensemble).
Partially nested designs (also known as partially clustered designs) are
designs where individuals in the treatment arm are assigned to clusters
(e.g., teachers, tutoring groups, therapists), whereas individuals in the
control arm have no such clustering.

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
