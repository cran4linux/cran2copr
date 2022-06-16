%global __brp_check_rpaths %{nil}
%global packname  moreparty
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          1%{?dist}%{?buildtag}
Summary:          A Toolbox for Conditional Inference Trees and Random Forests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-party 
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-CRAN-varImp 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-measures 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-iml 
BuildRequires:    R-CRAN-pdp 
BuildRequires:    R-CRAN-vip 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-rclipboard 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-datamods 
BuildRequires:    R-CRAN-phosphoricons 
Requires:         R-CRAN-party 
Requires:         R-CRAN-partykit 
Requires:         R-CRAN-varImp 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-measures 
Requires:         R-methods 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-iml 
Requires:         R-CRAN-pdp 
Requires:         R-CRAN-vip 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-rclipboard 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-datamods 
Requires:         R-CRAN-phosphoricons 

%description
Additions to 'party' and 'partykit' packages : tools for the
interpretation of forests (surrogate trees, prototypes, etc.), feature
selection (see Gregorutti et al (2017) <arXiv:1310.5726>, Hapfelmeier and
Ulm (2013) <doi:10.1016/j.csda.2012.09.020>, Altmann et al (2010)
<doi:10.1093/bioinformatics/btq134>) and parallelized versions of
conditional forest and variable importance functions. Also modules and a
shiny app for conditional inference trees.

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
