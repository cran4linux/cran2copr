%global __brp_check_rpaths %{nil}
%global packname  scpm
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          An R Package for Spatial Smoothing

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-stats 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-RandomFields 
BuildRequires:    R-CRAN-interp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-MASS 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-stats 
Requires:         R-Matrix 
Requires:         R-CRAN-RandomFields 
Requires:         R-CRAN-interp 
Requires:         R-methods 
Requires:         R-CRAN-rgl 
Requires:         R-lattice 
Requires:         R-CRAN-mvtnorm 
Requires:         R-MASS 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Group of functions for spatial smoothing using cubic splines and variogram
maximum likelihood estimation. Also allow the inclusion of linear
parametric terms and change-points for segmented smoothing splines models.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
