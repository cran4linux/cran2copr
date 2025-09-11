%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ravepipeline
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Reproducible Pipeline Infrastructure for Neuroscience

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fst >= 0.9.8
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-fastmap 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-promises 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-remotes 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-targets 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-logger 
Requires:         R-CRAN-fst >= 0.9.8
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-callr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-fastmap 
Requires:         R-CRAN-future 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-promises 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-remotes 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-targets 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-logger 

%description
Defines the underlying pipeline structure for reproducible neuroscience,
adopted by 'RAVE' (reproducible analysis and visualization of intracranial
electroencephalography); provides high-level class definition to build,
compile, set, execute, and share analysis pipelines. Both R and 'Python'
are supported, with 'Markdown' and 'shiny' dashboard templates for
extending and building customized pipelines. See the full documentations
at <https://rave.wiki>; to cite us, check out our paper by Magnotti, Wang,
and Beauchamp (2020, <doi:10.1016/j.neuroimage.2020.117341>), or run
citation("ravepipeline") for details.

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
