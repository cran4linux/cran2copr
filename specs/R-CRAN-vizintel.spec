%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vizintel
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Visualization Intelligence Toolkit

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-rlang 

%description
Provides automated data profiling and visualization recommendation tools
for exploratory data analysis (EDA). The package inspects a data frame,
classifies each variable as numeric, categorical, or datetime, and
computes distributional statistics including skewness, excess kurtosis,
Shapiro-Wilk normality test p-values (Royston 1995) <doi:10.2307/2986146>,
and cardinality. Based on these profiles, the package scores and ranks
candidate chart types (histogram, density, boxplot, violin, bar, lollipop,
scatter, hexbin, line, heatmap) using an internal taxonomy that accounts
for variable types, analysis goal, skewness, cardinality, and data size.
Additional functions audit existing ggplot objects for common
visualization integrity problems such as truncated axes, lie factors,
overplotting, and dual y-axes following principles described in Tufte
(1983, ISBN:0961392142) and Wilke (2019)
<https://clauswilke.com/dataviz/>. The package also checks visualizations
for accessibility issues and suggests alternative chart types for a given
plot.

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
