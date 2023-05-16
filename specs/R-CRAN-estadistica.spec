%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  estadistica
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Fundamentos De Estadistica Descriptiva e Inferencial

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rio 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-forecast 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rio 
Requires:         R-CRAN-data.table 
Requires:         R-grid 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-forecast 

%description
Este paquete pretende apoyar el proceso enseñanza-aprendizaje de
estadística descriptiva e inferencial. Las funciones contenidas en el
paquete 'estadistica' cubren los conceptos básicos estudiados en un curso
introductorio. Muchos conceptos son ilustrados con gráficos dinámicos o
web apps para facilitar su comprensión. This package aims to help the
teaching-learning process of descriptive and inferential statistics. The
functions contained in the package 'estadistica' cover the basic concepts
studied in a statistics introductory course. Many concepts are illustrated
with dynamic graphs or web apps to make the understanding easier. See:
Esteban et al. (2005, ISBN: 9788497323741), Newbold et al.(2019,
ISBN:9781292315034 ), Murgui et al. (2002, ISBN:9788484424673) .

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
