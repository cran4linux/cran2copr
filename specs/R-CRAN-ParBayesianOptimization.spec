%global __brp_check_rpaths %{nil}
%global packname  ParBayesianOptimization
%global packver   1.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Parallel Bayesian Optimization of Hyperparameters

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.11.8
BuildRequires:    R-CRAN-ggpubr >= 0.2.4
BuildRequires:    R-CRAN-DiceKriging 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-data.table >= 1.11.8
Requires:         R-CRAN-ggpubr >= 0.2.4
Requires:         R-CRAN-DiceKriging 
Requires:         R-stats 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-ggplot2 

%description
Fast, flexible framework for implementing Bayesian optimization of model
hyperparameters according to the methods described in Snoek et al.
<arXiv:1206.2944>. The package allows the user to run scoring function in
parallel, save intermediary results, and tweak other aspects of the
process to fully utilize the computing resources available to the user.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
