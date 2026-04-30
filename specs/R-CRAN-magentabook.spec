%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  magentabook
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          HM Treasury Magenta Book Policy Evaluation Primitives

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-stats 
Requires:         R-utils 

%description
Implements policy evaluation primitives from HM Treasury Magenta Book
guidance (HM Treasury, 2020): theory of change and log-frame construction,
evaluation planning and stakeholder mapping, power and
minimum-detectable-effect calculations for randomised designs (including
cluster and stepped-wedge designs following 'Hussey' and 'Hughes' (2007)
<doi:10.1016/j.cct.2006.05.007> and 'Hemming' et al. (2015)
<doi:10.1136/bmj.h391>), Maryland Scientific Methods Scale ratings,
structured confidence ratings, light-weight difference-in-differences and
interrupted-time-series estimators ('Bernal' et al. (2017)
<doi:10.1093/ije/dyw098>) with cluster-robust standard errors ('Cameron'
and 'Miller' (2015) <doi:10.3368/jhr.50.2.317>), pre-treatment balance
checks ('Stuart' (2010) <doi:10.1214/09-STS313>), and cost-effectiveness
analysis (cost per outcome, incremental cost-effectiveness ratio,
acceptability curves, incremental net benefit, quality-adjusted and
disability-adjusted life years). Designed as the evaluation companion to
the appraisal package 'greenbook'. Bundled rubric and reference tables
carry vintage metadata for reproducibility.

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
