%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mycaas
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          My Computerized Adaptive Assessment

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rPref 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-igraph 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rPref 
Requires:         R-CRAN-shiny 
Requires:         R-stats 

%description
Implementation of adaptive assessment procedures based on Knowledge Space
Theory (KST, Doignon & Falmagne, 1999 <ISBN:9783540645016>) and Formal
Psychological Assessment (FPA, Spoto, Stefanutti & Vidotto, 2010
<doi:10.3758/BRM.42.1.342>) frameworks. An adaptive assessment is a type
of evaluation that adjusts the difficulty and nature of subsequent
questions based on the test taker's responses to previous ones. The
package contains functions to perform and simulate an adaptive assessment.
Moreover, it is integrated with two 'Shiny' interfaces, making it both
accessible and user-friendly.  The package has been partially funded by
the European Union - NextGenerationEU and by the Ministry of University
and Research (MUR), National Recovery and Resilience Plan (NRRP), Mission
4, Component 2, Investment 1.5, project “RAISE - Robotics and AI for
Socio-economic Empowerment” (ECS00000035).

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
