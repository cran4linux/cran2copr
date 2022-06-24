%global __brp_check_rpaths %{nil}
%global packname  DeltaMAN
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Delta Measurement of Agreement for Nominal Data

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyMatrix 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyMatrix 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-knitr 

%description
Analysis of agreement for nominal data between two raters using the Delta
model. This model is proposed as an alternative to the widespread measure
Cohen kappa coefficient, which performs poorly when the marginal
distributions are very asymmetric (Martin-Andres and Femia-Marzo (2004),
<doi:10.1348/000711004849268>; Martin-Andres and Femia-Marzo (2008)
<doi:10.1080/03610920701669884>). The package also contains a function to
perform a massive analysis of multiple raters against a gold standard. A
shiny app is also provided to obtain the measures of nominal agreement
between two raters.

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
