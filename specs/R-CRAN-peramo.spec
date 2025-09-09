%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  peramo
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Permutation Tests for Randomization Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-emmeans >= 1.8.6
BuildRequires:    R-CRAN-lme4 >= 1.1.33
BuildRequires:    R-CRAN-dplyr >= 1.1.2
BuildRequires:    R-CRAN-parameters >= 0.21.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-emmeans >= 1.8.6
Requires:         R-CRAN-lme4 >= 1.1.33
Requires:         R-CRAN-dplyr >= 1.1.2
Requires:         R-CRAN-parameters >= 0.21.0
Requires:         R-stats 
Requires:         R-utils 

%description
Perform permutation-based hypothesis testing for randomized experiments as
suggested in Ludbrook & Dudley (1998) <doi:10.2307/2685470> and Ernst
(2004) <doi:10.1214/088342304000000396>, introduced in Pham et al. (2022)
<doi:10.1016/j.chemosphere.2022.136736>.

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
