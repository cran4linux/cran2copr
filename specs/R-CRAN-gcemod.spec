%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gcemod
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Competing Event Models with Lunn-McNeil Testing

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.2
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-cmprsk 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.5.2
Requires:         R-CRAN-survival 
Requires:         R-CRAN-cmprsk 
Requires:         R-CRAN-patchwork 
Requires:         R-stats 

%description
Fits generalized competing event (GCE) models and estimates covariate
effects on omega-plus, the ratio of the hazard for an event of interest to
the hazard for a competing event, on both the cause-specific (Cox) and
subdistribution (Fine-Gray) hazard scales. Confidence intervals and
p-values are obtained from the Lunn-McNeil (1995) stacked (augmented) data
approach. The package builds GCE risk scores from the model linear
predictor, identifies risk-score cutpoints that maximize the separation in
omega-plus between groups, and produces cumulative incidence ("alligator")
plots by risk group and calibration plots of predicted versus observed
omega-plus. It also compares covariate effects across the primary,
competing, and total (composite) events, and estimates covariate effects
on the ratio of cumulative incidence functions (a
cumulative-incidence-scale GCE model). Methods follow Carmona et al.
(2014) <doi:10.1016/j.ijrobp.2014.03.047>, Mell et al. (2024)
<doi:10.1016/j.eururo.2023.01.020>, and Lunn and McNeil (1995)
<doi:10.2307/2532940>.

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
