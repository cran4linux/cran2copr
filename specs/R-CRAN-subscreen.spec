%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  subscreen
%global packver   4.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Systematic Screening of Study Data for Subgroup Effects

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-bsplus 
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-shinyWidgets 
Requires:         R-utils 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-DT 
Requires:         R-stats 
Requires:         R-CRAN-shinyjs 
Requires:         R-methods 
Requires:         R-CRAN-bsplus 
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-shinyWidgets 

%description
Identifying outcome relevant subgroups has now become as simple as
possible! The formerly lengthy and tedious search for the needle in a
haystack will be replaced by a single, comprehensive and coherent
presentation. The central result of a subgroup screening is a diagram in
which each single dot stands for a subgroup. The diagram may show
thousands of them. The position of the dot in the diagram is determined by
the sample size of the subgroup and the statistical measure of the
treatment effect in that subgroup. The sample size is shown on the
horizontal axis while the treatment effect is displayed on the vertical
axis. Furthermore, the diagram shows the line of no effect and the overall
study results. For small subgroups, which are found on the left side of
the plot, larger random deviations from the mean study effect are
expected, while for larger subgroups only small deviations from the study
mean can be expected to be chance findings. So for a study with no
conspicuous subgroup effects, the dots in the figure are expected to form
a kind of funnel. Any deviations from this funnel shape hint to
conspicuous subgroups.

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
