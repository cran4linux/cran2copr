%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tricolore
%global packver   1.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          A Flexible Color Scale for Ternary Compositions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 4.0.0
BuildRequires:    R-CRAN-ggtern >= 4.0.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-assertthat 
Requires:         R-CRAN-ggplot2 >= 4.0.0
Requires:         R-CRAN-ggtern >= 4.0.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-grDevices 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-assertthat 

%description
Compositional data consisting of three-parts can be color mapped with a
ternary color scale. Such a scale is provided by the tricolore packages
with options for discrete and continuous colors, mean-centering and
scaling. See Jonas Schöley (2021) "The centered ternary balance scheme. A
technique to visualize surfaces of unbalanced three-part compositions"
<doi:10.4054/DemRes.2021.44.19>, Jonas Schöley, Frans Willekens (2017)
"Visualizing compositional data on the Lexis surface"
<doi:10.4054/DemRes.2017.36.21>, and Ilya Kashnitsky, Jonas Schöley (2018)
"Regional population structures at a glance"
<doi:10.1016/S0140-6736(18)31194-2>.

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
