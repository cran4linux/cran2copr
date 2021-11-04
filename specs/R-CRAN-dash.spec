%global __brp_check_rpaths %{nil}
%global packname  dash
%global packver   0.9.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.2
Release:          1%{?dist}%{?buildtag}
Summary:          An Interface to the Dash Ecosystem for Authoring Reactive Web Applications

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-reqres >= 0.2.3
BuildRequires:    R-CRAN-fiery > 1.0.0
BuildRequires:    R-CRAN-routr > 0.2.0
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-mime 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-brotli 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-httpuv 
Requires:         R-CRAN-reqres >= 0.2.3
Requires:         R-CRAN-fiery > 1.0.0
Requires:         R-CRAN-routr > 0.2.0
Requires:         R-CRAN-R6 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-mime 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-brotli 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-utils 
Requires:         R-CRAN-httpuv 

%description
A framework for building analytical web applications, Dash offers a
pleasant and productive development experience. No JavaScript required.

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
