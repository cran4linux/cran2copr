%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  beezdiscounting
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Behavioral Economic Easy Discounting

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-beezdemand 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-beezdemand 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
Facilitates some of the analyses performed in studies of behavioral
economic discounting. The package supports scoring of the 27-Item Monetary
Choice Questionnaire (see Kaplan et al., 2016;
<doi:10.1007/s40614-016-0070-9>), calculating k values (Mazur's simple
hyperbolic and exponential) using nonlinear regression, calculating
various Area Under the Curve (AUC) measures, plotting regression curves
for both fit-to-group and two-stage approaches, checking for unsystematic
discounting (Johnson & Bickel, 2008; <doi:10.1037/1064-1297.16.3.264>) and
scoring of the minute discounting task (see Koffarnus & Bickel, 2014;
<doi:10.1037/a0035973>) using the Qualtrics 5-trial discounting template
(see the Qualtrics Minute Discounting User Guide;
<doi:10.13140/RG.2.2.26495.79527>), which is also available as a .qsf file
in this package.

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
