%global packname  biotools
%global packver   3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1
Release:          3%{?dist}%{?buildtag}
Summary:          Tools for Biometry and Applied Statistics in AgriculturalScience

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15
Requires:         R-core >= 2.15
BuildArch:        noarch
BuildRequires:    R-CRAN-rpanel 
BuildRequires:    R-CRAN-tkrplot 
BuildRequires:    R-MASS 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-SpatialEpi 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-boot 
BuildRequires:    R-grDevices 
BuildRequires:    R-datasets 
Requires:         R-CRAN-rpanel 
Requires:         R-CRAN-tkrplot 
Requires:         R-MASS 
Requires:         R-lattice 
Requires:         R-CRAN-SpatialEpi 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-boot 
Requires:         R-grDevices 
Requires:         R-datasets 

%description
Tools designed to perform and work with cluster analysis (including
Tocher's algorithm), discriminant analysis and path analysis (standard and
under collinearity), as well as some useful miscellaneous tools for
dealing with sample size and optimum plot size calculations. Mantel's
permutation test can be found in this package. A new approach for
calculating its power is implemented. biotools also contains the new tests
for genetic covariance components. An approach for predicting spatial gene
diversity is implemented.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
