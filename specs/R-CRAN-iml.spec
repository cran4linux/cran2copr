%global __brp_check_rpaths %{nil}
%global packname  iml
%global packver   0.11.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.11.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interpretable Machine Learning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Metrics 
BuildRequires:    R-CRAN-prediction 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Metrics 
Requires:         R-CRAN-prediction 
Requires:         R-CRAN-R6 

%description
Interpretability methods to analyze the behavior and predictions of any
machine learning model.  Implemented methods are: Feature importance
described by Fisher et al. (2018) <arXiv:1801.01489>, accumulated local
effects plots described by Apley (2018) <arXiv:1612.08468>, partial
dependence plots described by Friedman (2001)
<www.jstor.org/stable/2699986>, individual conditional expectation ('ice')
plots described by Goldstein et al.  (2013)
<doi:10.1080/10618600.2014.907095>, local models (variant of 'lime')
described by Ribeiro et. al (2016) <arXiv:1602.04938>, the Shapley Value
described by Strumbelj et. al (2014) <doi:10.1007/s10115-013-0679-x>,
feature interactions described by Friedman et. al <doi:10.1214/07-AOAS148>
and tree surrogate models.

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
