%global packname  subscreen
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}
Summary:          Systematic Screening of Study Data for Subgroup Effects

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-bsplus 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-randomForestSRC 
BuildRequires:    R-CRAN-V8 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-shinyWidgets 
Requires:         R-utils 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-data.table 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-DT 
Requires:         R-stats 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-bsplus 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-randomForestSRC 
Requires:         R-CRAN-V8 
Requires:         R-CRAN-purrr 
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
conspicuous subgroups. This approach was presented in Muysers (2020)
<doi:10.1007/s43441-019-00082-6> and referenced in Ballarini (2020)
<doi:10.1002/pst.2012>. New to version 3 is the Automatic Screening of
one- or MUlti-factorial Subgroups (ASMUS) for documentation of the
structured review of subgroup findings.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
