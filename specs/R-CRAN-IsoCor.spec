%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  IsoCor
%global packver   0.1.40
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.40
Release:          1%{?dist}%{?buildtag}
Summary:          Analyze Isotope Ratios in a 'Shiny'-App

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.50
Requires:         R-core >= 3.50
BuildArch:        noarch
BuildRequires:    R-CRAN-bsplus 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-golem 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-MALDIquant 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyalert 
BuildRequires:    R-CRAN-shinyjs 
Requires:         R-CRAN-bsplus 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-golem 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-MALDIquant 
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyalert 
Requires:         R-CRAN-shinyjs 

%description
Analyzing Inductively Coupled Plasma - Mass Spectrometry (ICP-MS)
measurement data to evaluate isotope ratios (IRs) is a complex process.
The 'IsoCor' package facilitates this process and renders it reproducible
by providing a function to run a 'Shiny'-App locally in any web browser.
In this App the user can upload data files of various formats, select ion
traces, apply peak detection and perform calculation of IRs and delta
values. Results are provided as figures and tables and can be exported.
The App, therefore, facilitates data processing of ICP-MS experiments to
quickly obtain optimal processing parameters compared to traditional
'Excel' worksheet based approaches. A more detailed description can be
found in the corresponding article "Data processing made easy: standalone
tool for automated calculation of isotope ratio from transient signals –
IsoCor" by Tukhmetova et al. in Journal of Analytical Atomic Spectrometry
(JAAS). The most recent version of 'IsoCor' can be tested online at
<https://jali.shinyapps.io/isocor>.

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
