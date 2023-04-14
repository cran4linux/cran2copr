%global __brp_check_rpaths %{nil}
%global packname  ScottKnottESD
%global packver   2.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          The Scott-Knott Effect Size Difference (ESD) Test

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-effsize 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-forecast 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-effsize 
Requires:         R-stats 
Requires:         R-CRAN-car 
Requires:         R-CRAN-forecast 

%description
The Scott-Knott Effect Size Difference (ESD) test is a mean comparison
approach that leverages a hierarchical clustering to partition the set of
treatment means (e.g., means of variable importance scores, means of model
performance) into statistically distinct groups with non-negligible
difference [Tantithamthavorn et al., (2018)
<doi:10.1109/TSE.2018.2794977>].

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
