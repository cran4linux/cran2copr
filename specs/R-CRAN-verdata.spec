%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  verdata
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analyze Data from the Truth Commission in Colombia

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-arrow 
BuildRequires:    R-CRAN-assertr 
BuildRequires:    R-base 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-LCMCR 
BuildRequires:    R-CRAN-logger 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-tools 
Requires:         R-CRAN-arrow 
Requires:         R-CRAN-assertr 
Requires:         R-base 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-LCMCR 
Requires:         R-CRAN-logger 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-tools 

%description
Facilitates use and analysis of data about the armed conflict in Colombia
resulting from the joint project between La Jurisdicción Especial para la
Paz (JEP), La Comisión para el Esclarecimiento de la Verdad, la
Convivencia y la No repetición (CEV), and the Human Rights Data Analysis
Group (HRDAG). The data are 100 replicates from a multiple imputation
through chained equations as described in Van Buuren and
Groothuis-Oudshoorn (2011) <doi:10.18637/jss.v045.i03>. With the
replicates the user can examine four human rights violations that occurred
in the Colombian conflict accounting for the impact of missing fields and
fully missing observations.

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
