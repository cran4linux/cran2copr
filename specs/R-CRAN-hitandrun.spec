%global packname  hitandrun
%global packver   0.5-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.5
Release:          1%{?dist}
Summary:          "Hit and Run" and "Shake and Bake" for Sampling Uniformly fromConvex Shapes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-rcdd >= 1.1
BuildRequires:    R-stats 
Requires:         R-CRAN-rcdd >= 1.1
Requires:         R-stats 

%description
The "Hit and Run" Markov Chain Monte Carlo method for sampling uniformly
from convex shapes defined by linear constraints, and the "Shake and Bake"
method for sampling from the boundary of such shapes. Includes specialized
functions for sampling normalized weights with arbitrary linear
constraints.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
