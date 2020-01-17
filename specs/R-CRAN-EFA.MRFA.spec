%global packname  EFA.MRFA
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          1%{?dist}
Summary:          Dimensionality Assessment Using Minimum Rank Factor Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-optimbase 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-PCovR 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-CRAN-optimbase 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-PCovR 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 

%description
Performs parallel analysis (Timmerman & Lorenzo-Seva, 2011
<doi:10.1037/a0023353>) and hull method (Lorenzo-Seva, Timmerman, & Kiers,
2011 <doi:10.1080/00273171.2011.564527>) for assessing the dimensionality
of a set of variables using minimum rank factor analysis (see ten Berge &
Kiers, 1991 <doi:10.1007/BF02294464> for more information). The package
also includes the option to compute minimum rank factor analysis by
itself, as well as the greater lower bound calculation.

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
