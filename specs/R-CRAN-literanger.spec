%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  literanger
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Random Forests for Multiple Imputation Based on 'ranger'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-Rcereal >= 1.3.2
BuildRequires:    R-CRAN-cpp11 >= 0.4.7
BuildRequires:    R-stats 
Requires:         R-stats 

%description
An updated implementation of R package 'ranger' by Wright et al, (2017)
<doi:10.18637/jss.v077.i01> for training and predicting from random
forests, particularly suited to high-dimensional data, and for embedding
in 'Multiple Imputation by Chained Equations' (MICE) by van Buuren (2007)
<doi:10.1177/0962280206074463>. Ensembles of classification and regression
trees are currently supported. Sparse data of class 'dgCMatrix' (R package
'Matrix') can be directly analyzed. Conventional bagged predictions are
available alongside an efficient prediction for MICE via the algorithm
proposed by Doove et al (2014) <doi:10.1016/j.csda.2013.10.025>. Survival
and probability forests are not supported in the update, nor is data of
class 'gwaa.data' (R package 'GenABEL'); use the original 'ranger' package
for these analyses.

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
