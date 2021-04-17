%global packname  outliertree
%global packver   1.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Explainable Outlier Detection Through Decision Tree Conditioning

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-Rcereal 
Requires:         R-CRAN-Rcpp >= 1.0.1

%description
Will try to fit decision trees that try to "predict" values for each
column based on the values of each other column. Along the way, each time
a split is evaluated, it will take the observations that fall into each
branch as a homogeneous cluster in which it will search for outliers in
the 1-d distribution of the column being predicted. Outliers are
determined according to confidence intervals in this 1-d distribution, and
need to have a large gap with respect to the next observation in sorted
order to be flagged as outliers. Since outliers are searched for in a
decision tree branch, it will know the conditions that make it a rare
observation compared to others that meet the same conditions, and the
conditions will always be correlated with the target variable (as it's
being predicted from them). Full procedure is described in Cortes (2020)
<arXiv:2001.00636>. Loosely based on the 'GritBot'
<https://www.rulequest.com/gritbot-info.html> software.

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
