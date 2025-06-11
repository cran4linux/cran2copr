%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  reservoirnet
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Reservoir Computing and Echo State Networks

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-testthat >= 3.0.0
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
Requires:         R-CRAN-testthat >= 3.0.0
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 

%description
A simple user-friendly library based on the 'python' module 'reservoirpy'.
It provides a flexible interface to implement efficient Reservoir
Computing (RC) architectures with a particular focus on Echo State
Networks (ESN). Some of its features are: offline and online training,
parallel implementation, sparse matrix computation, fast spectral
initialization, advanced learning rules (e.g. Intrinsic Plasticity) etc.
It also makes possible to easily create complex architectures with
multiple reservoirs (e.g. deep reservoirs), readouts, and complex feedback
loops. Moreover, graphical tools are included to easily explore
hyperparameters. Finally, it includes several tutorials exploring time
series forecasting, classification and hyperparameter tuning. For more
information about 'reservoirpy', please see Trouvain et al. (2020)
<doi:10.1007/978-3-030-61616-8_40>. This package was developed in the
framework of the University of Bordeaux’s IdEx "Investments for the
Future" program / RRI PHDS.

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
