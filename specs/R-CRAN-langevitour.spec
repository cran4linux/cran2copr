%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  langevitour
%global packver   0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Langevin Tour

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-crosstalk 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-assertthat 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-crosstalk 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-assertthat 

%description
An HTML widget that randomly tours 2D projections of numerical data. A
random walk through projections of the data is shown. The user can
manipulate the plot to use specified axes, or turn on Guided Tour mode to
find an informative projection of the data. Groups within the data can be
hidden or shown, as can particular axes. Points can be brushed, and the
selection can be linked to other widgets using crosstalk. The underlying
method to produce the random walk and projection pursuit uses Langevin
dynamics. The widget can be used from within R, or included in a
self-contained R Markdown or Quarto document or presentation, or used in a
Shiny app.

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
