%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  drawsample
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Draw Samples with the Desired Properties from a Data Set

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-xlsx 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-xlsx 
Requires:         R-utils 

%description
A tool to sample data with the desired properties.Samples can be drawn by
purposive sampling with determining distributional conditions, such as
deviation from normality (skewness and kurtosis), and sample size in
quantitative research studies. For purposive sampling, a researcher has
something in mind and participants that fit the purpose of the study are
included (Etikan,Musa, & Alkassim, 2015)
<doi:10.11648/j.ajtas.20160501.11>.Purposive sampling can be useful for
answering many research questions (Klar & Leeper, 2019)
<doi:10.1002/9781119083771.ch21>.

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
