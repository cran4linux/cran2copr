%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shinydisconnect
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Show a Nice Message When a 'Shiny' App Disconnects or Errors

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.0
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-htmltools 
Requires:         R-CRAN-shiny >= 1.0
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-htmltools 

%description
A 'Shiny' app can disconnect for a variety of reasons: an unrecoverable
error occurred in the app, the server went down, the user lost internet
connection, or any other reason that might cause the 'Shiny' app to lose
connection to its server. With 'shinydisconnect', you can call
disonnectMessage() anywhere in a Shiny app's UI to add a nice message when
this happens. Works locally (running Shiny apps within 'RStudio') and on
Shiny servers (such as shinyapps.io, 'RStudio Connect', 'Shiny Server Open
Source', 'Shiny Server Pro'). See demo online at
<https://daattali.com/shiny/shinydisconnect-demo/>.

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
