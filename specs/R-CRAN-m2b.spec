%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  m2b
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Movement to Behaviour Inference using Random Forest

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-caTools 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-caret 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-stats 

%description
Prediction of behaviour from movement characteristics using observation
and random forest for the analyses of movement data in ecology. From
movement information (speed, bearing...) the model predicts the observed
behaviour (movement, foraging...) using random forest. The model can then
extrapolate behavioural information to movement data without direct
observation of behaviours. The specificity of this method relies on the
derivation of multiple predictor variables from the movement data over a
range of temporal windows. This procedure allows to capture as much
information as possible on the changes and variations of movement and
ensures the use of the random forest algorithm to its best capacity. The
method is very generic, applicable to any set of data providing movement
data together with observation of behaviour.

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
