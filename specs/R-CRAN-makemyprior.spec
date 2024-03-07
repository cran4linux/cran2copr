%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  makemyprior
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Intuitive Construction of Joint Priors for Variance Parameters

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-visNetwork 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-MASS 

%description
Tool for easy prior construction and visualization. It helps to formulates
joint prior distributions for variance parameters in latent Gaussian
models. The resulting prior is robust and can be created in an intuitive
way. A graphical user interface (GUI) can be used to choose the joint
prior, where the user can click through the model and select priors. An
extensive guide is available in the GUI. The package allows for direct
inference with the specified model and prior. Using a hierarchical
variance decomposition, we formulate a joint variance prior that takes the
whole model structure into account. In this way, existing knowledge can
intuitively be incorporated at the level it applies to. Alternatively, one
can use independent variance priors for each model components in the
latent Gaussian model.

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
