%global packname  BCA1SG
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Block Coordinate Ascent with One-Step Generalized RosenAlgorithm

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-logOfGamma 
BuildRequires:    R-stats 
Requires:         R-Matrix 
Requires:         R-CRAN-logOfGamma 
Requires:         R-stats 

%description
Implementing the Block Coordinate Ascent with One-Step Generalized Rosen
(BCA1SG) algorithm on the semiparametric models for panel count data,
interval-censored survival data, and degradation data. A comprehensive
description of the BCA1SG algorithm can be found in Wang et al. (2020)
<https://github.com/yudongstat/BCA1SG/blob/master/BCA1SG.pdf>. For details
of the semiparametric models for panel count data, interval-censored
survival data, and degradation data, please see Wellner and Zhang (2007)
<doi:10.1214/009053607000000181>, Huang and Wellner (1997)
<ISBN:978-0-387-94992-5>, and Wang and Xu (2010)
<doi:10.1198/TECH.2009.08197>, respectively.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
