%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  esmtools
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Preprocessing Experience Sampling Method (ESM) Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-lubridate >= 1.9.0
BuildRequires:    R-CRAN-jsonlite >= 1.8.0
BuildRequires:    R-CRAN-fs >= 1.6.0
BuildRequires:    R-CRAN-stringr >= 1.5.0
BuildRequires:    R-CRAN-knitr >= 1.43
BuildRequires:    R-CRAN-kableExtra >= 1.3.0
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-ggpubr >= 0.6.0
BuildRequires:    R-CRAN-DT >= 0.28
BuildRequires:    R-CRAN-base64enc >= 0.1.3
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-lubridate >= 1.9.0
Requires:         R-CRAN-jsonlite >= 1.8.0
Requires:         R-CRAN-fs >= 1.6.0
Requires:         R-CRAN-stringr >= 1.5.0
Requires:         R-CRAN-knitr >= 1.43
Requires:         R-CRAN-kableExtra >= 1.3.0
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-ggpubr >= 0.6.0
Requires:         R-CRAN-DT >= 0.28
Requires:         R-CRAN-base64enc >= 0.1.3
Requires:         R-grDevices 
Requires:         R-CRAN-htmltools 
Requires:         R-stats 
Requires:         R-tools 

%description
Tailored explicitly for Experience Sampling Method (ESM) data, it contains
a suite of functions designed to simplify preprocessing steps and create
subsequent reporting. It empowers users with capabilities to extract
critical insights during preprocessing, conducts thorough data quality
assessments (e.g., design and sampling scheme checks, compliance rate,
careless responses), and generates visualizations and concise summary
tables tailored specifically for ESM data. Additionally, it streamlines
the creation of informative and interactive preprocessing reports,
enabling researchers to transparently share their dataset preprocessing
methodologies. Finally, it is part of a larger ecosystem which includes a
framework and a web gallery (<https://preprocess.esmtools.com/>).

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
