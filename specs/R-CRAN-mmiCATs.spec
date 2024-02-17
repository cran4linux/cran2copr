%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mmiCATs
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Cluster Adjusted t Statistic Applications

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-broom.mixed 
BuildRequires:    R-CRAN-clusterSEs 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mmcards 
BuildRequires:    R-CRAN-robust 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinythemes 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-broom.mixed 
Requires:         R-CRAN-clusterSEs 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-lmerTest 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mmcards 
Requires:         R-CRAN-robust 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinythemes 

%description
Simulation results detailed in Esarey and Menger (2019)
<doi:10.1017/psrm.2017.42> demonstrate that cluster adjusted t statistics
(CATs) are an effective method for correcting standard errors in scenarios
with a small number of clusters. The 'mmiCATs' package offers a suite of
tools for working with CATs. The mmiCATs() function initiates a 'shiny'
web application, facilitating the analysis of data utilizing CATs, as
implemented in the cluster.im.glm() function from the 'clusterSEs'
package. Additionally, the pwr_func_lmer() function is designed to
simplify the process of conducting simulations to compare mixed effects
models with CATs models. For educational purposes, the CloseCATs()
function launches a 'shiny' application card game, aimed at enhancing
users' understanding of the conditions under which CATs should be
preferred over random intercept models.

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
