%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  kernelshap
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Kernel SHAP

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-foreach 
Requires:         R-stats 
Requires:         R-utils 

%description
Multidimensional refinement of the Kernel SHAP algorithm described in Ian
Covert and Su-In Lee (2021) <http://proceedings.mlr.press/v130/covert21a>.
The package allows to calculate Kernel SHAP values in an exact way, by
iterative sampling (as in the reference above), or by a hybrid of the two.
As soon as sampling is involved, the algorithm iterates until convergence,
and standard errors are provided.  The package works with any model that
provides numeric predictions of dimension one or higher.  Examples include
linear regression, logistic regression (on logit or probability scale),
other generalized linear models, generalized additive models, and neural
networks.  The package plays well together with meta-learning packages
like 'tidymodels', 'caret' or 'mlr3'. Visualizations can be done using the
R package 'shapviz'.

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
