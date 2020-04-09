%global packname  casen
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}
Summary:          Metodos De Estimacion Con Disenio Probabilistico y Estratificadoen Encuesta CASEN (Estimation Methods with ProbabilisticStratified Sampling in CASEN Survey)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-labelled 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-srvyr 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-labelled 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-srvyr 
Requires:         R-CRAN-purrr 

%description
Funciones para realizar estadistica descriptiva e inferencia con el
disenio complejo de la Encuesta CASEN (Encuesta de Caracterizacion
Socio-Economica). Incluye datasets que permiten armonizar los codigos de
comunas que cambian entre anios y permite convertir a los codigos
oficiales de SUBDERE. (Functions to compute descriptive and inferential
statistics with CASEN Survey [Socio-Economic Characterization Survey]
complex design. Includes datasets to harmonize commune codes that change
across years and allows to convert to official SUBDERE codes.)

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
