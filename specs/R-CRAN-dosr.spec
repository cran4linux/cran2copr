%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dosr
%global packver   0.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.4
Release:          1%{?dist}%{?buildtag}
Summary:          Survey Analysis Tools for the Chilean Social Observatory

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-srvyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-labelled 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-srvyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-future 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-labelled 
Requires:         R-CRAN-tibble 

%description
Provides high-level functions to compute estimates (means, proportions,
totals, ratios and quantiles) for complex survey designs, with automatic
classification of statistical reliability, between-year significance tests
and standardised report generation in 'Excel' format (via 'openxlsx'). It
was developed for the Social Observatory ('Observatorio Social') of the
Chilean Ministry of Social Development and implements its data-quality
criteria, but it can be applied to any complex-survey design (for example
the Chilean 'CASEN' household survey, included as example data). The
reliability criteria follow Division Observatorio Social (2023)
<https://bidat.gob.cl/details/ficha/dato/manual-para-la-investigacion-casen-2022>
and Instituto Nacional de Estadisticas (2020)
<https://www.ine.gob.cl/inicio/documentos-de-trabajo/documento/fundamentos-del-est%%C3%%A1ndar-para-la-evaluaci%%C3%%B3n-de-la-calidad-de-las-estimaciones-en-encuestas-de-hogares>;
complex-survey estimation methods follow Lumley (2010,
ISBN:9780470284308).

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
