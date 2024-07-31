%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shinycssloaders
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Add Loading Animations to a 'shiny' Output While It's Recalculating

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-htmltools >= 0.3.5
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-htmltools >= 0.3.5
Requires:         R-CRAN-digest 
Requires:         R-CRAN-glue 
Requires:         R-grDevices 
Requires:         R-CRAN-shiny 

%description
When a 'Shiny' output (such as a plot, table, map, etc.) is recalculating,
it remains visible but gets greyed out. Using 'shinycssloaders', you can
add a loading animation ("spinner") to outputs instead. By wrapping a
'Shiny' output in 'withSpinner()', a spinner will automatically appear
while the output is recalculating. You can also manually show and hide the
spinner, or add a full-page spinner to cover the entire page. See the demo
online at <https://daattali.com/shiny/shinycssloaders-demo/>.

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
