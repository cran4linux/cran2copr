%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  parttree
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Visualize Simple 2-D Decision Tree Partitions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tinyplot >= 0.3.0
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rpart 
Requires:         R-CRAN-tinyplot >= 0.3.0
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-partykit 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rpart 

%description
Visualize the partitions of simple decision trees, involving one or two
predictors, on the scale of the original data. Provides an intuitive
alternative to traditional tree diagrams, by visualizing how a decision
tree divides the predictor space in a simple 2D plot alongside the
original data. The 'parttree' package supports both classification and
regression trees from 'rpart' and 'partykit', as well as trees produced by
popular frontend systems like 'tidymodels' and 'mlr3'. Visualization
methods are provided for both base R graphics and 'ggplot2'.

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
