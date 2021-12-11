%global __brp_check_rpaths %{nil}
%global packname  stepgbm
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Stepwise Variable Selection for Generalized Boosted Regression Modeling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-spm 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-steprf 
Requires:         R-CRAN-spm 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-steprf 

%description
An introduction to a couple of novel predictive variable selection methods
for generalised boosted regression modeling (gbm). They are based on
various variable influence methods (i.e., relative variable influence
(RVI) and knowledge informed RVI (i.e., KIRVI, and KIRVI2)) that adopted
similar ideas as AVI, KIAVI and KIAVI2 in the 'steprf' package, and also
based on predictive accuracy in stepwise algorithms. For details of the
variable selection methods, please see: Li, J., Siwabessy, J., Huang, Z.
and Nichol, S. (2019) <doi:10.3390/geosciences9040180>. Li, J., Alvarez,
B., Siwabessy, J., Tran, M., Huang, Z., Przeslawski, R., Radke, L.,
Howard, F., Nichol, S. (2017). <DOI: 10.13140/RG.2.2.27686.22085>.

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
