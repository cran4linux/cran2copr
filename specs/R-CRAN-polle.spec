%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  polle
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
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
BuildRequires:    R-CRAN-data.table >= 1.14.5
BuildRequires:    R-CRAN-SuperLearner 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-targeted 
BuildRequires:    R-CRAN-DynTxRegime 
Requires:         R-CRAN-lava >= 1.7.0
Requires:         R-CRAN-policytree >= 1.2.0
Requires:         R-CRAN-data.table >= 1.14.5
Requires:         R-CRAN-SuperLearner 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-progressr 
Requires:         R-methods 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-targeted 
Requires:         R-CRAN-DynTxRegime 

%description
Framework for evaluating user-specified finite stage policies and learning
realistic policies via doubly robust loss functions. Policy learning
methods include doubly robust restricted Q-learning, sequential policy
tree learning and outcome weighted learning. See Nordland and Holst (2022)
<arXiv:2212.02335> for documentation and references.

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
