%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  trajmsm
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Marginal Structural Models with Latent Class Growth Analysis of Treatment Trajectories

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-flexmix 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-flexmix 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-sandwich 
Requires:         R-utils 

%description
Implements marginal structural models combined with a latent class growth
analysis framework for assessing the causal effect of treatment
trajectories. Based on the approach described in "Marginal Structural
Models with Latent Class Growth Analysis of Treatment Trajectories" Diop,
A., Sirois, C., Guertin, J.R., Schnitzer, M.E., Candas, B., Cossette, B.,
Poirier, P., Brophy, J., Mésidor, M., Blais, C. and Hamel, D., (2023)
<doi:10.1177/09622802231202384>.

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
