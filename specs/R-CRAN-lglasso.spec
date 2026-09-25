%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lglasso
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Graphical Lasso for Longitudinal Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-CVXR 
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-fake 
BuildRequires:    R-stats 
Requires:         R-CRAN-CVXR 
Requires:         R-CRAN-glasso 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-fake 
Requires:         R-stats 

%description
Estimate treatment-specific precision matrices (networks) from
longitudinal high-dimensional normal data. The corresponding random
effects are also estimated. It is motivated by the analysis of omics data
in clinical trials where the longitudinal omics data becomes increasingly
common. It includes both one-stage models (without treatment) and
two-stage models (with one treatment). For details of the algorithms,
please check the materials on its GitHub repo. If you have any questions,
feel free to contact the maintainers through the email below.

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
