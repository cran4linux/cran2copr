%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  glmnetSE
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Add Nonparametric Bootstrap SE to 'glmnet' for Selected Coefficients (No Shrinkage)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-graphics 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-glmnet 
Requires:         R-graphics 
Requires:         R-parallel 
Requires:         R-stats 

%description
Builds a LASSO, Ridge, or Elastic Net model with 'glmnet' or 'cv.glmnet'
with bootstrap inference statistics (SE, CI, and p-value) for selected
coefficients with no shrinkage applied for them. Model performance can be
evaluated on test data and an automated alpha selection is implemented for
Elastic Net. Parallelized computation is used to speed up the process. The
methods are described in Friedman et al. (2010)
<doi:10.18637/jss.v033.i01> and Simon et al. (2011)
<doi:10.18637/jss.v039.i05>.

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
