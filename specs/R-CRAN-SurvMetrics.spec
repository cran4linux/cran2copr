%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SurvMetrics
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Predictive Evaluation Metrics in Survival Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-survminer 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-pec 
BuildRequires:    R-CRAN-randomForestSRC 
Requires:         R-CRAN-survminer 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-pec 
Requires:         R-CRAN-randomForestSRC 

%description
An implementation of popular evaluation metrics that are commonly used in
survival prediction including Concordance Index, Brier Score, Integrated
Brier Score, Integrated Square Error, Integrated Absolute Error and Mean
Absolute Error. For a detailed information, see (Ishwaran H, Kogalur UB,
Blackstone EH and Lauer MS (2008) <doi:10.1214/08-AOAS169>) and (Moradian
H, Larocque D and Bellavance F (2017) <doi:10.1007/s10985-016-9372-1>) for
different evaluation metrics.

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
