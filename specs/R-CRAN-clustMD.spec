%global __brp_check_rpaths %{nil}
%global packname  clustMD
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Model Based Clustering for Mixed Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.2
Requires:         R-core >= 3.3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-reshape2 
Requires:         R-MASS 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-mvtnorm 
Requires:         R-parallel 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-viridis 
Requires:         R-stats 

%description
Model-based clustering of mixed data (i.e. data which consist of
continuous, binary, ordinal or nominal variables) using a parsimonious
mixture of latent Gaussian variable models.

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
