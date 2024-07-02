%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  matchMulti
%global packver   1.1.12.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.12.1
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Multilevel Matching using a Network Algorithm

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-rcbsubset >= 1.1.4
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-coin 
BuildRequires:    R-CRAN-weights 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-rcbsubset >= 1.1.4
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-coin 
Requires:         R-CRAN-weights 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-magrittr 

%description
Performs multilevel matches for data with cluster- level treatments and
individual-level outcomes using a network optimization algorithm.
Functions for checking balance at the cluster and individual levels are
also provided, as are methods for permutation-inference-based outcome
analysis.  Details in Pimentel et al. (2018) <doi:10.1214/17-AOAS1118>.
The optmatch package, which is useful for running many of the provided
functions, may be downloaded from Github at
<https://github.com/markmfredrickson/optmatch> if not available on CRAN.

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
