%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  polle
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Policy Learning

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lava >= 1.7.0
BuildRequires:    R-CRAN-policytree >= 1.2.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-SuperLearner 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-targeted 
Requires:         R-CRAN-lava >= 1.7.0
Requires:         R-CRAN-policytree >= 1.2.0
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-future.apply 
Requires:         R-methods 
Requires:         R-CRAN-SuperLearner 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-targeted 

%description
Framework for evaluating and learning realistic policies based on doubly
robust loss functions. Policy learning methods include Q-learning, see
Tsiatis et al. (2019) <doi:10.1201/9780429192692>, (doubly robust)
V-restricted Q-learning, see Luedtke & van der Laan (2016)
<doi:10.1515/ijb-2015-0052>, and (doubly robust) sequential policy tree
learning, see Zhou et al. <arXiv:1810.04778>.

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
