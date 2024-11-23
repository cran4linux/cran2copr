%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  jointVIP
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Prioritize Variables with Joint Variable Importance Plot in Observational Study Design

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-ggrepel >= 0.9.2
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-ggrepel >= 0.9.2

%description
In the observational study design stage, matching/weighting methods are
conducted. However, when many background variables are present, the
decision as to which variables to prioritize for matching/weighting is not
trivial. Thus, the joint treatment-outcome variable importance plots are
created to guide variable selection. The joint variable importance plots
enhance variable comparisons via unadjusted bias curves derived under the
omitted variable bias framework. The plots translate variable importance
into recommended values for tuning parameters in existing methods.
Post-matching and/or weighting plots can also be used to visualize and
assess the quality of the observational study design. The method
motivation and derivation is presented in "Prioritizing Variables for
Observational Study Design using the Joint Variable Importance Plot" by
Liao et al. (2024) <doi:10.1080/00031305.2024.2303419>. See the package
paper by Liao and Pimentel (2024) <doi:10.21105/joss.06093> for a beginner
friendly user introduction.

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
