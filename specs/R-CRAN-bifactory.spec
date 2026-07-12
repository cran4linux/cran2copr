%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bifactory
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          (Bifactor) ESEM with Continuous (MLR) or Ordered (WLSMV) Data

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan >= 0.6.21
BuildRequires:    R-CRAN-GPArotation 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-lavaan >= 0.6.21
Requires:         R-CRAN-GPArotation 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-numDeriv 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-withr 

%description
Fits bifactor exploratory structural equation models (B-ESEM), together
with standard exploratory structural equation modeling (ESEM) and
confirmatory factor analysis (CFA), for continuous and ordered-categorical
data. Continuous models use 'lavaan' native efa() blocks with robust
maximum likelihood (MLR) estimation. Ordered-categorical ESEM defaults to
the 'lavaan' weighted least squares mean- and variance-adjusted (WLSMV)
estimator; ordered B-ESEM uses a custom diagonally weighted least squares
(DWLS) path with polychoric correlations from 'psych', rotation-delta
standard errors via 'numDeriv', and a mean- and variance-adjusted
chi-square. Target, geomin, and oblimin rotations use 'GPArotation'; the
bifactor ESEM approach follows Morin, Arens and Marsh (2016)
<doi:10.1080/10705511.2014.961800>. Additional features include
multi-group measurement invariance (configural through strict, with
partial invariance), ESEM-within-CFA conversion, McDonald's omega
reliability suite, and the Mehrvarz and Rouder (2026)
<doi:10.31234/osf.io/95enc_v3> alignment ratio check for independent
cluster model confirmatory factor analysis (ICM-CFA) misspecification. An
optional 'MplusAutomation' interface allows side-by-side comparison with
'Mplus' output.

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
