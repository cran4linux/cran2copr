%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fairness
%global packver   1.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Algorithmic Fairness Metrics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pROC 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pROC 

%description
Offers calculation, visualization and comparison of algorithmic fairness
metrics. Fair machine learning is an emerging topic with the overarching
aim to critically assess whether ML algorithms reinforce existing social
biases. Unfair algorithms can propagate such biases and produce
predictions with a disparate impact on various sensitive groups of
individuals (defined by sex, gender, ethnicity, religion, income,
socioeconomic status, physical or mental disabilities). Fair algorithms
possess the underlying foundation that these groups should be treated
similarly or have similar prediction outcomes. The fairness R package
offers the calculation and comparisons of commonly and less commonly used
fairness metrics in population subgroups. These methods are described by
Calders and Verwer (2010) <doi:10.1007/s10618-010-0190-x>, Chouldechova
(2017) <doi:10.1089/big.2016.0047>, Feldman et al. (2015)
<doi:10.1145/2783258.2783311> , Friedler et al. (2018)
<doi:10.1145/3287560.3287589> and Zafar et al. (2017)
<doi:10.1145/3038912.3052660>. The package also offers convenient
visualizations to help understand fairness metrics.

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
