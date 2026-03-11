%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ROOT
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Rashomon Set of Optimal Trees

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-rpart.plot 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-gbm 
Requires:         R-stats 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-rpart.plot 

%description
Implements a general framework for globally optimizing user-specified
objective functionals over interpretable binary weight functions
represented as sparse decision trees, called ROOT (Rashomon Set of Optimal
Trees). It searches over candidate trees to construct a Rashomon set of
near-optimal solutions and derives a summary tree highlighting stable
patterns in the optimized weights. ROOT includes a built-in
generalizability mode for identifying subgroups in trial settings for
transportability analyses (Parikh et al. (2025)
<doi:10.1080/01621459.2025.2495319>).

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
