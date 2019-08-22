%global packname  anipaths
%global packver   0.9.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.7
Release:          1%{?dist}
Summary:          Animation of Observed Trajectories Using Spline-BasedInterpolation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-animation 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-mgcv 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-ggmap 
Requires:         R-CRAN-animation 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-rgdal 
Requires:         R-mgcv 
Requires:         R-grDevices 
Requires:         R-CRAN-ggmap 

%description
Animation of observed trajectories using spline-based interpolation (see
for example, Buderman, F. E., Hooten, M. B., Ivan, J. S. and Shenk, T. M.
(2016), <doi:10.1111/2041-210X.12465> "A functional model for
characterizing long-distance movement behaviour". Methods Ecol Evol).
Intended to be used exploratory data analysis, and perhaps for preparation
of presentations.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
