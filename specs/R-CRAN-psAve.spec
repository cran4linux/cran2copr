%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  psAve
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Model-Averaged Propensity Scores Selected by Prognostic-Score Balance

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-cobalt >= 4.6.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
Requires:         R-CRAN-cobalt >= 4.6.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 

%description
Constructs a model-averaged propensity score as a convex combination of
candidate propensity score models, with mixing weights selected on a
simplex grid to optimize covariate or prognostic-score balance,
implementing the method of Kabata, Stuart and Shintani (2024)
<doi:10.1186/s12874-024-02350-y>. Prognostic scores follow Hansen (2008)
<doi:10.1093/biomet/asn004>: outcome models are fit on untreated units
only. The resulting score is designed to be supplied directly to the
matchit() function of 'MatchIt' as a distance measure or to the weightit()
function of 'WeightIt' as a propensity score, with balance assessment via
'cobalt'.

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
