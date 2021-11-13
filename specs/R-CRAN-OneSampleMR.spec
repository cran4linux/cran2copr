%global __brp_check_rpaths %{nil}
%global packname  OneSampleMR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          One Sample Mendelian Randomization and Instrumental Variable Analyses

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-gmm 
BuildRequires:    R-CRAN-ivreg 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-msm 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-gmm 
Requires:         R-CRAN-ivreg 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-msm 

%description
Useful functions for one-sample (individual level data) Mendelian
randomization and instrumental variable analyses. The package includes
implementations of; the Sanderson and Windmeijer (2016)
<doi:10.1016/j.jeconom.2015.06.004> conditional F-statistic, the
multiplicative structural mean model Hernán and Robins (2006)
<doi:10.1097/01.ede.0000222409.00878.37>, and two-stage predictor
substitution and two-stage residual inclusion estimators explained by
Terza et al. (2008) <doi:10.1016/j.jhealeco.2007.09.009>.

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
