%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  burakDiagrams
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Burak Diagrams for Model Performance Evaluation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-scales 
Requires:         R-stats 

%description
Creates interactive 3D Burak Diagrams for evaluating climatological and
hydrological simulations. The BD-Clim framework evaluates climatological
simulations by representing correlation, standard deviation, centered root
mean-square difference, bias, and root mean-square difference. The
BD-HydNSE framework evaluates hydrological simulations using correlation,
standard deviation, centered root mean-square difference, percent bias,
and Nash-Sutcliffe efficiency. The BD-HydKGE framework evaluates
hydrological simulations using correlation, standard deviation, centered
root mean-square difference, percent bias, and Kling-Gupta efficiency. The
frameworks extend the Taylor Diagram ( Taylor (2001)
<doi:10.1029/2000JD900719> ) by introducing an orthogonal axis for bias
and representing selected performance metrics as surfaces in the resulting
3D space. Nash-Sutcliffe efficiency was introduced by Nash and Sutcliffe
(1970) <doi:10.1016/0022-1694(70)90255-6>, and Kling-Gupta efficiency was
proposed by Gupta et al. (2009) <doi:10.1016/j.jhydrol.2009.08.003>. The
diagrams are interactive and can optionally be saved as HTML files.

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
