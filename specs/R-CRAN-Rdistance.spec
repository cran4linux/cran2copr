%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rdistance
%global packver   4.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Density and Abundance from Distance-Sampling Surveys

License:          GNU General Public License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-units 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-dfoptim 
BuildRequires:    R-CRAN-expint 
BuildRequires:    R-CRAN-multidplyr 
Requires:         R-CRAN-units 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-dfoptim 
Requires:         R-CRAN-expint 
Requires:         R-CRAN-multidplyr 

%description
Distance-sampling (<doi:10.1007/978-3-319-19219-2>) is a field survey and
analytical method that estimates density and abundance of survey targets
(e.g., animals) when detection probability declines with observation
distance. Distance-sampling is popular in ecology, especially when survey
targets are observed from aerial platforms (e.g., airplane or drone),
surface vessels (e.g., boat or truck), or along walking transects.
Analysis involves fitting smooth (parametric) curves to histograms of
observation distances and using those functions to adjust density
estimates for missed targets.  Routines included here fit curves to
observation distance histograms, estimate effective sampling area, density
of targets in surveyed areas, and the abundance of targets in a
surrounding study area. Confidence interval estimation uses built-in
bootstrap resampling. Help files are extensive and have been vetted by
multiple authors. Many tutorials are available on the package's website
(URL below).

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
