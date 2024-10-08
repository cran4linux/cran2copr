%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nonlinearICP
%global packver   0.1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Invariant Causal Prediction for Nonlinear Models

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-CondIndTests 
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-CRAN-randomForest 
Requires:         R-methods 
Requires:         R-CRAN-CondIndTests 
Requires:         R-CRAN-data.tree 
Requires:         R-CRAN-caTools 
Requires:         R-CRAN-randomForest 

%description
Performs 'nonlinear Invariant Causal Prediction' to estimate the causal
parents of a given target variable from data collected in different
experimental or environmental conditions, extending 'Invariant Causal
Prediction' from Peters, Buehlmann and Meinshausen (2016),
<arXiv:1501.01332>, to nonlinear settings. For more details, see C.
Heinze-Deml, J. Peters and N. Meinshausen: 'Invariant Causal Prediction
for Nonlinear Models', <arXiv:1706.08576>.

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
