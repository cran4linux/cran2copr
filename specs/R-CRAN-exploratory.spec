%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  exploratory
%global packver   0.3.31
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.31
Release:          1%{?dist}%{?buildtag}
Summary:          A Tool for Large-Scale Exploratory Analyses

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-lemon 
BuildRequires:    R-CRAN-lm.beta 
BuildRequires:    R-CRAN-mediation 
BuildRequires:    R-CRAN-remotes 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-weights 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-lemon 
Requires:         R-CRAN-lm.beta 
Requires:         R-CRAN-mediation 
Requires:         R-CRAN-remotes 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-weights 

%description
Conduct numerous exploratory analyses in an instant with a point-and-click
interface. With one simple command, this tool launches a Shiny App on the
local machine. Drag and drop variables in a data set to categorize them as
possible independent, dependent, moderating, or mediating variables. Then
run dozens (or hundreds) of analyses instantly to uncover any
statistically significant relationships among variables. Any relationship
thus uncovered should be tested in follow-up studies. This tool is
designed only to facilitate exploratory analyses and should NEVER be used
for p-hacking. Many of the functions used in this package are previous
versions of functions in the R Packages 'kim' and 'ezr'. Selected
References: Chang et al. (2021)
<https://CRAN.R-project.org/package=shiny>. Dowle et al. (2021)
<https://CRAN.R-project.org/package=data.table>. Kim (2023)
<https://jinkim.science/docs/kim.pdf>. Kim (2021)
<doi:10.5281/zenodo.4619237>. Kim (2020)
<https://CRAN.R-project.org/package=ezr>. Simmons et al. (2011)
<doi:10.1177/0956797611417632> Tingley et al. (2019)
<https://CRAN.R-project.org/package=mediation>. Wickham et al. (2020)
<https://CRAN.R-project.org/package=ggplot2>.

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
