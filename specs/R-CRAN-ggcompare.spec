%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggcompare
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Mean Comparison in 'ggplot2'

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-ggplot2 

%description
Add mean comparison annotations to a 'ggplot'. This package provides an
easy way to indicate if two or more groups are significantly different in
a 'ggplot'. Usually you do not need to specify the test method, you only
need to tell stat_compare() whether you want to perform a parametric test
or a nonparametric test, and stat_compare() will automatically choose the
appropriate test method based on your data. For comparisons between two
groups, the p-value is calculated by t-test (parametric) or Wilcoxon rank
sum test (nonparametric). For comparisons among more than two groups, the
p-value is calculated by One-way ANOVA (parametric) or Kruskal-Wallis test
(nonparametric).

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
