%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  modelskill
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Assessing and Visualising the Performance of Prediction Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-viridis 

%description
Provides tools for evaluating continuous predictions and their associated
predictive uncertainty from statistical, machine-learning, geostatistical,
and process-based models. It implements complementary measures of
prediction error, association, agreement, efficiency, uncertainty
calibration, and predictive-distribution performance, together with
Taylor, solar, target, coverage, probability integral transform, and
quantile-coverage diagnostics. Methods include the integrated evaluation
approach of Wadoux, Walvoort and Brus (2022)
<doi:10.1016/j.geoderma.2021.115332> and the uncertainty-validation
framework of Schmidinger and Heuvelink (2023)
<doi:10.1016/j.geoderma.2023.116585>.

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
