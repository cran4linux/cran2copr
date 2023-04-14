%global __brp_check_rpaths %{nil}
%global packname  ggfan
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Summarise a Distribution Through Coloured Intervals

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-rstan 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-grid 
Requires:         R-CRAN-rstan 

%description
Implements the functionality of the 'fanplot' package as 'geoms' for
'ggplot2'. Designed for summarising MCMC samples from a posterior
distribution, where a visualisation is desired for several values of a
continuous covariate. Increasing posterior intervals of the sampled
quantity are mapped to a continuous colour scale.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
