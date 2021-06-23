%global __brp_check_rpaths %{nil}
%global packname  ArchaeoPhases
%global packver   1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Post-Processing of the Markov Chain Simulated by 'ChronoModel', 'Oxcal' or 'BCal'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-hdrcde 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-CRAN-toOrdinal 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggalt 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-hdrcde 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-ggthemes 
Requires:         R-CRAN-toOrdinal 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggalt 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 

%description
Provides a list of functions for the statistical analysis of
archaeological dates and groups of dates. It is based on the
post-processing of the Markov Chains whose stationary distribution is the
posterior distribution of a series of dates. Such output can be simulated
by different applications as for instance 'ChronoModel' (see
<https://chronomodel.com/>), 'Oxcal' (see
<https://c14.arch.ox.ac.uk/oxcal.html>) or 'BCal' (see
<https://bcal.shef.ac.uk/>). The only requirement is to have a csv file
containing a sample from the posterior distribution.  Note that this
package interacts with data available through the 'ArchaeoPhases.dataset'
package which is available in a separate repository.  The size of the
'ArchaeoPhases.dataset' package is approximately 4 MB.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
