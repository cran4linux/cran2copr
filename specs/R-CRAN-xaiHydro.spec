%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  xaiHydro
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Explainable AI Tools for Hydro-Climate Modelling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-DALEX >= 2.4.0
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-patchwork >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-DALEX >= 2.4.0
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-patchwork >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang >= 1.1.0

%description
Provides a unified workflow for applying Explainable Artificial
Intelligence (XAI) methods to hydro-climate predictive models. Functions
implement a permutation-based Monte Carlo SHAP estimator (Strumbelj and
Kononenko (2014) <doi:10.1007/s10115-013-0679-x>; Lundberg and Lee (2017)
<doi:10.48550/arXiv.1705.07874>), a self-contained locally weighted linear
surrogate LIME (Ribeiro et al. (2016) <doi:10.1145/2939672.2939778>), and
Partial Dependence Plots with Accumulated Local Effects (Friedman (2001)
<doi:10.1214/aos/1013203451>; Apley and Zhu (2020)
<doi:10.1111/rssb.12377>) with hydrology-specific visualisations and
interpretation utilities. Supports any model object compatible with the
'DALEX' explainer interface (Biecek (2018) <doi:10.18637/jss.v097.i01>),
including random forests, gradient boosting, and neural networks trained
on streamflow, drought indices, flood risk, or evapotranspiration data.
Hydrology-standard performance metrics Nash-Sutcliffe Efficiency (NSE,
Nash and Sutcliffe (1970) <doi:10.1016/0022-1694(70)90255-6>) and
Kling-Gupta Efficiency (KGE, Gupta et al. (2009)
<doi:10.1016/j.jhydrol.2009.08.003>) are computed alongside standard
regression metrics. Designed to accompany the book chapter: Islam, S.,
Dheeraj, A., Ali, S., Kaushal, R. and Venkatesh, G. (2026). Explainable
Artificial Intelligence for Hydro-Climatic Modelling: Methods,
Applications, and Implementation Using the xaiHydro R Package. In
Chandniha, S. K. et al. (Eds.), Hydro-Climate Analytics: Remote Sensing,
AI and Geospatial Modelling. Springer.

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
