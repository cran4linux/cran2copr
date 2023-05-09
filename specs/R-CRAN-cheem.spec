%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cheem
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interactively Explore Local Explanations with the Radial Tour

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-spinifex >= 0.3.3
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-conflicted 
Requires:         R-CRAN-spinifex >= 0.3.3
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-conflicted 

%description
Given a tree-based machine learning model, calculate the tree SHAP
<arXiv:1802.03888>; <https://github.com/ModelOriented/treeshap> local
explanation of every observation. View the data space, explanation space,
and model residuals as ensemble graphic interactive on a shiny
application. After an observation of interest is identified, the
normalized variable importance of the local explanation is used as a 1D
projection basis. The support of the local explanation is then explored by
changing the basis with the use of the radial tour
<doi:10.32614/RJ-2020-027>; <doi:10.1080/10618600.1997.10474754>.

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
