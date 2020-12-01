%global packname  vardpoor
%global packver   0.20.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.20.1
Release:          1%{?dist}%{?buildtag}
Summary:          Variance Estimation for Sample Surveys by the Ultimate Cluster Method

License:          EUPL | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.12.6
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-surveyplanning 
BuildRequires:    R-CRAN-laeken 
Requires:         R-CRAN-data.table >= 1.12.6
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-surveyplanning 
Requires:         R-CRAN-laeken 

%description
Generation of domain variables, linearization of several non-linear
population statistics (the ratio of two totals, weighted income
percentile, relative median income ratio, at-risk-of-poverty rate,
at-risk-of-poverty threshold, Gini coefficient, gender pay gap, the
aggregate replacement ratio, the relative median income ratio, median
income below at-risk-of-poverty gap, income quintile share ratio, relative
median at-risk-of-poverty gap), computation of regression residuals in
case of weight calibration, variance estimation of sample surveys by the
ultimate cluster method (Hansen, Hurwitz and Madow, Sample Survey Methods
And Theory, vol. I: Methods and Applications; vol. II: Theory. 1953, New
York: John Wiley and Sons), variance estimation for longitudinal,
cross-sectional measures and measures of change for single and multistage
stage cluster sampling designs (Berger, Y. G., 2015,
<doi:10.1111/rssa.12116>). Several other precision measures are derived -
standard error, the coefficient of variation, the margin of error,
confidence interval, design effect.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
