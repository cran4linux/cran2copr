%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  idcnrba
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Application for Analyzing Representativeness and Nonresponse Bias

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survey >= 4.1.1
BuildRequires:    R-CRAN-rstudioapi >= 0.5
BuildRequires:    R-CRAN-DT >= 0.28
BuildRequires:    R-CRAN-nrba >= 0.2.0
BuildRequires:    R-CRAN-miniUI >= 0.1.1
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-flexdashboard 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-srvyr 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-base64enc 
Requires:         R-CRAN-survey >= 4.1.1
Requires:         R-CRAN-rstudioapi >= 0.5
Requires:         R-CRAN-DT >= 0.28
Requires:         R-CRAN-nrba >= 0.2.0
Requires:         R-CRAN-miniUI >= 0.1.1
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-shiny 
Requires:         R-stats 
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-flexdashboard 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-srvyr 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-base64enc 

%description
Provides access to the Idea Data Center (IDC) application for conducting
nonresponse bias analysis (NRBA). The IDC NRBA app is an interactive,
browser-based Shiny application that can be used to analyze survey data
with respect to response rates, representativeness, and nonresponse bias.
This app provides a user-friendly interface to statistical methods
implemented by the 'nrba' package. Krenzke, Van de Kerckhove, and Mohadjer
(2005) <http://www.asasrms.org/Proceedings/y2005/files/JSM2005-000572.pdf>
and Lohr and Riddles (2016)
<https://www150.statcan.gc.ca/n1/en/pub/12-001-x/2016002/article/14677-eng.pdf?st=q7PyNsGR>
provide an overview of the statistical methods implemented in the
application.

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
