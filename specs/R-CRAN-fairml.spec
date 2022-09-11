%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fairml
%global packver   0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7
Release:          1%{?dist}%{?buildtag}
Summary:          Fair Models in Machine Learning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-optiSolve 
BuildRequires:    R-CRAN-CVXR 
BuildRequires:    R-CRAN-glmnet 
Requires:         R-methods 
Requires:         R-CRAN-optiSolve 
Requires:         R-CRAN-CVXR 
Requires:         R-CRAN-glmnet 

%description
Fair machine learning regression models which take sensitive attributes
into account in model estimation. Currently implementing Komiyama et al.
(2018) <http://proceedings.mlr.press/v80/komiyama18a/komiyama18a.pdf>,
Zafar et al. (2019)
<https://www.jmlr.org/papers/volume20/18-262/18-262.pdf> and my own
approach that uses ridge regression to enforce fairness.

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
