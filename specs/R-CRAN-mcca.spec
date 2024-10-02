%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mcca
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Category Classification Accuracy

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-rgl 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-rgl 

%description
It contains six common multi-category classification accuracy evaluation
measures. All of these measures could be found in Li and Ming (2019)
<doi:10.1002/sim.8103>. Specifically, Hypervolume Under Manifold (HUM),
described in Li and Fine (2008) <doi:10.1093/biostatistics/kxm050>.
Correct Classification Percentage (CCP), Integrated Discrimination
Improvement (IDI), Net Reclassification Improvement (NRI), R-Squared Value
(RSQ), described in Li, Jiang and Fine (2013)
<doi:10.1093/biostatistics/kxs047>. Polytomous Discrimination Index (PDI),
described in Van Calster et al. (2012) <doi:10.1007/s10654-012-9733-3>. Li
et al. (2018) <doi:10.1177/0962280217692830>. We described all these above
measures and our mcca package in Li, Gao and D'Agostino (2019)
<doi:10.1002/sim.8103>.

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
