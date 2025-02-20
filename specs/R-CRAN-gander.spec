%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gander
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          High Performance, Low Friction Large Language Model Chat

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.3
BuildRequires:    R-CRAN-shiny >= 1.9.1
BuildRequires:    R-CRAN-glue >= 1.8.0
BuildRequires:    R-CRAN-rlang >= 1.1.4
BuildRequires:    R-CRAN-rstudioapi >= 0.17.1
BuildRequires:    R-CRAN-miniUI >= 0.1.1.1
BuildRequires:    R-CRAN-ellmer >= 0.1.0
BuildRequires:    R-CRAN-streamy 
BuildRequires:    R-CRAN-treesitter 
BuildRequires:    R-CRAN-treesitter.r 
Requires:         R-CRAN-cli >= 3.6.3
Requires:         R-CRAN-shiny >= 1.9.1
Requires:         R-CRAN-glue >= 1.8.0
Requires:         R-CRAN-rlang >= 1.1.4
Requires:         R-CRAN-rstudioapi >= 0.17.1
Requires:         R-CRAN-miniUI >= 0.1.1.1
Requires:         R-CRAN-ellmer >= 0.1.0
Requires:         R-CRAN-streamy 
Requires:         R-CRAN-treesitter 
Requires:         R-CRAN-treesitter.r 

%description
Introduces a 'Copilot'-like completion experience, but it knows how to
talk to the objects in your R environment. 'ellmer' chats are integrated
directly into your 'RStudio' and 'Positron' sessions, automatically
incorporating relevant context from surrounding lines of code and your
global environment (like data frame columns and types). Open the package
dialog box with a keyboard shortcut, type your request, and the assistant
will stream its response directly into your documents.

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
