%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  forestat
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Forest Carbon Sequestration and Potential Productivity Calculation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-CRAN-nlme 
Requires:         R-stats 
Requires:         R-CRAN-rlang 

%description
Include assessing site classes based on the stand height growth and
establishing a nonlinear mixed-effect biomass model under different site
classes based on the whole stand model to achieve more accurate estimation
of carbon sequestration. In particular, a carbon sequestration potential
productivity calculation method based on the potential mean annual
increment is proposed. This package is applicable to both natural forests
and plantations. It can quantitatively assess stand’s potential
productivity, realized productivity, and possible improvement under
certain site, and can be used in many aspects such as site quality
assessment, tree species suitability evaluation, and forest degradation
evaluation. Reference: Lei X, Fu L, Li H, et al (2018)
<doi:10.11707/j.1001-7488.20181213>. Fu L, Sharma R P, Zhu G, et al (2017)
<doi:10.3390/f8040119>.

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
