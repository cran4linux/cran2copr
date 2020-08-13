%global packname  fragility
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Assessing and Visualizing Fragility of Clinical Results withBinary Outcomes

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotrix >= 3.7.5
BuildRequires:    R-graphics >= 3.5.0
BuildRequires:    R-grDevices >= 3.5.0
BuildRequires:    R-stats >= 3.5.0
BuildRequires:    R-CRAN-metafor >= 2.0.0
BuildRequires:    R-CRAN-netmeta >= 1.0.0
Requires:         R-CRAN-plotrix >= 3.7.5
Requires:         R-graphics >= 3.5.0
Requires:         R-grDevices >= 3.5.0
Requires:         R-stats >= 3.5.0
Requires:         R-CRAN-metafor >= 2.0.0
Requires:         R-CRAN-netmeta >= 1.0.0

%description
A collection of user-friendly functions for assessing and visualizing
fragility of individual studies (Walsh et al., 2014
<doi:10.1016/j.jclinepi.2013.10.019>; Lin, 2020 <doi:10.1111/jep.13428>),
conventional pairwise meta-analyses (Atal et al., 2019
<doi:10.1016/j.jclinepi.2019.03.012>), and network meta-analyses of
multiple treatments with binary outcomes (Xing et al., 2020
<doi:10.1016/j.jclinepi.2020.07.003>). The included functions are designed
to: 1) calculate the fragility index (i.e., the minimal event status
modifications that can alter the significance or non-significance of the
original result) and fragility quotient (i.e., fragility index divided by
sample size) at a specific significance level; 2) give the cases of event
status modifications for altering the result's significance or
non-significance and visualize these cases; 3) visualize the trend of
statistical significance as event status is modified; 4) efficiently
derive fragility indexes and fragility quotients at multiple significance
levels, and visualize the relationship between these fragility measures
against the significance levels; and 5) calculate fragility indexes and
fragility quotients of multiple datasets (e.g., a collection of clinical
trials or meta-analyses) and produce plots of their overall distributions.
The outputs from these functions may inform the robustness of clinical
results in terms of statistical significance and aid the interpretation of
fragility measures.

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
