%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BsplineQuantRegGui
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive 'Shiny' Interface for 'BsplineQuantReg'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.6.0
Requires:         R-core >= 4.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-BsplineQuantReg >= 0.2.5
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-ECOSolveR 
Requires:         R-CRAN-BsplineQuantReg >= 0.2.5
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-png 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-ECOSolveR 

%description
A user-friendly interactive Shiny interface for the 'BsplineQuantReg'
package, enabling quantile regression using B-splines with shape
constraints, based on the method described in Abbes (2025). Almost all
parameters of the main function 'quantile_spline()' can be tuned. Features
include interactive knot placement, per-region constraint specification,
'CSV' data import, direct demo access, reproducible R code generation, and
solver selection. The version 0.2.2 handles knots multiplicity, Bspline
basis visualisation, mean-square regression, pp form visualisation under
human readable form, in local or canonical bases, The GUI provides two
modes, basic (compatible with 'BsplineQuantReg' >= 0.2.2) and advanced
(requires 'BsplineQuantReg' >= 0.2.5 for stable multiplicity features).
This GUI an improved version of the 'Python Tk' version of
'BsplineQuantRegPy'.

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
