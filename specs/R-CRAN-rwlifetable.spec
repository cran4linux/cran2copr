%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rwlifetable
%global packver   0.1.0-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of Life Tables Using Rolling Windows

License:          EPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-splines 
Requires:         R-stats 
Requires:         R-splines 

%description
Estimates life tables, specifically (crude) death rates and (raw and
graduated) death probabilities, using rolling windows in one (e.g., age),
two (e.g., age and time) or three (e.g., age, time and income) dimensions.
The package can also be utilised for summarising statistics and smoothing
continuous variables through rolling windows in other domains, such as
estimating averages of self-positioning ideology in political science.
Acknowledgements: The authors wish to thank Ministerio de Ciencia,
Innovación y Universidades (grant PID2021-128228NB-I00) and Generalitat
Valenciana (grants HIECPU/2023/2, Conselleria de Hacienda, Economía y
Administración Pública, and CIGE/2023/7, Conselleria de Educación,
Cultura, Universidades y Empleo) for supporting this research.

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
