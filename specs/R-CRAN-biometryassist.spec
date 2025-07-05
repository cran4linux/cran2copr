%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  biometryassist
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Functions to Assist Design and Analysis of Agronomic Experiments

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-agricolae 
BuildRequires:    R-CRAN-askpass 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-multcompView 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-agricolae 
Requires:         R-CRAN-askpass 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-multcompView 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-xml2 

%description
Provides functions to aid in the design and analysis of agronomic and
agricultural experiments through easy access to documentation and helper
functions, especially for users who are learning these concepts. While not
required for most functionality, this package enhances the `asreml`
package which provides a computationally efficient algorithm for fitting
mixed models using Residual Maximum Likelihood. It is a commercial package
that can be purchased as 'asreml-R' from 'VSNi' <https://vsni.co.uk/>, who
will supply a zip file for local installation/updating (see
<https://asreml.kb.vsni.co.uk/>).

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
