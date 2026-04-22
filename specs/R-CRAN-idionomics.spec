%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  idionomics
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Conduct Idionomic Analyses for Time Series Modeling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
A toolkit for idionomic science, a research philosophy that places the
unit of the ensemble (individual/couple/group) at the center of analysis.
Rather than assuming a common distribution, a similar enough process for
each unit, and fitting a single model to the whole ensemble, idionomic
methods model each unit separately, then aggregate upward if sensible. The
group-level picture emerges from individual results, not the other way
around, while explicitly evaluating whether aggregation is reasonable
given the measured level of heterogeneity of effects. The package is built
around intensive longitudinal data where each participant contributes a
time series. It provides a pipeline from preprocessing through modeling to
group-level summaries. Current functions: data quality screening
(i_screener()), within-person standardization (pmstandardize()), linear
detrending (i_detrender()), per-subject ARIMAX (AutoRegressive Integrated
Moving Average with eXogenous inputs) modeling and meta-analysis
(iarimax()), individual p-values (i_pval()), Sign Divergence and
Equisyncratic Null tests (sden_test()), and directed loop detection
(looping_machine()). Methods are described in Hernandez et al. (2024)
<doi:10.1007/978-3-030-77644-2_136-1>, Ciarrochi et al. (2024)
<doi:10.1007/s10608-024-10486-w>, and Sahdra et al. (2024)
<doi:10.1016/j.jcbs.2024.100728>.

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
