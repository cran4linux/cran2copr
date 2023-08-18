%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DominoDataR
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          'Domino Data R SDK'

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-arrow 
BuildRequires:    R-CRAN-ConfigParser 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-reticulate 
Requires:         R-CRAN-arrow 
Requires:         R-CRAN-ConfigParser 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-reticulate 

%description
A wrapper on top of the 'Domino Data Python SDK' library. It lets you
query and access 'Domino Data Sources' directly from your R environment.
Under the hood, 'Domino Data R SDK' leverages the API provided by the
'Domino Data Python SDK', which must be installed as a prerequisite.
'Domino' is a platform that makes it easy to run your code on scalable
hardware, with integrated version control and collaboration features
designed for analytical workflows. See
<https://docs.dominodatalab.com/en/latest/api_guide/140b48/domino-data-api>
for more information.

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
