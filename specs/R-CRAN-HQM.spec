%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HQM
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Superefficient Estimation of Future Conditional Hazards Based on Marker Information

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-pec 
BuildRequires:    R-CRAN-timeROC 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-JM 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-pec 
Requires:         R-CRAN-timeROC 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-JM 

%description
Provides a nonparametric smoothed kernel estimator for the future
conditional hazard rate function when time-dependent covariates are
present, a bandwidth selector for the estimator's implementation and
pointwise and uniform confidence bands. Methods used in the package refer
to Bagkavos, Isakson, Mammen, Nielsen and Proust-Lima (2025)
<doi:10.1093/biomet/asaf008>.

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
