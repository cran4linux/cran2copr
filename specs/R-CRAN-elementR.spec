%global packname  elementR
%global packver   1.3.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.7
Release:          1%{?dist}%{?buildtag}
Summary:          An Framework for Reducing Elemental LAICPMS Data from Solid Structures

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-gnumeric 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-tcltk2 
BuildRequires:    R-CRAN-reader 
BuildRequires:    R-CRAN-readODS 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-EnvStats 
BuildRequires:    R-CRAN-outliers 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-httpuv 
Requires:         R-CRAN-gdata 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-gnumeric 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-lmtest 
Requires:         R-tcltk 
Requires:         R-CRAN-tcltk2 
Requires:         R-CRAN-reader 
Requires:         R-CRAN-readODS 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-EnvStats 
Requires:         R-CRAN-outliers 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-colourpicker 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-httpuv 

%description
Aims to facilitate the reduction of elemental microchemistry data from
solid-phase LAICPMS analysis (laser ablation inductive coupled plasma mass
spectrometry). The 'elementR' package provides a reactive and user
friendly interface (based on a 'shiny' application) and a set of 'R6'
classes for conducting all steps needed for an optimal data reduction
while leaving maximum control for user. For more details about the methods
used in 'elementR', see Sirot et al (2017) <DOI:10.1111/2041-210X.12822>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
