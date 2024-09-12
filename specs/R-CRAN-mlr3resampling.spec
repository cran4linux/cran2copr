%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mlr3resampling
%global packver   2024.9.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2024.9.6
Release:          1%{?dist}%{?buildtag}
Summary:          Resampling Algorithms for 'mlr3' Framework

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-paradox 
BuildRequires:    R-CRAN-mlr3 
BuildRequires:    R-CRAN-mlr3misc 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-paradox 
Requires:         R-CRAN-mlr3 
Requires:         R-CRAN-mlr3misc 

%description
A supervised learning algorithm inputs a train set, and outputs a
prediction function, which can be used on a test set. If each data point
belongs to a group (such as geographic region, year, etc), then how do we
know if it is possible to train on one group, and predict accurately on
another group? Cross-validation can be used to determine the extent to
which this is possible, by first assigning fold IDs from 1 to K to all
data (possibly using stratification, usually by group and label). Then we
loop over test sets (group/fold combinations), train sets (same group,
other groups, all groups), and compute test/prediction accuracy for each
combination.  Comparing test/prediction accuracy between same and other,
we can determine the extent to which it is possible (perfect if same/other
have similar test accuracy for each group; other is usually somewhat less
accurate than same; other can be just as bad as featureless baseline when
the groups have different patterns). For more information,
<https://tdhock.github.io/blog/2023/R-gen-new-subsets/> describes the
method in depth. How many train samples are required to get accurate
predictions on a test set? Cross-validation can be used to answer this
question, with variable size train sets.

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
