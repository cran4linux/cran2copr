%global packname  vcdExtra
%global packver   0.7-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.1
Release:          3%{?dist}
Summary:          'vcd' Extensions and Additions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-gnm >= 1.0.3
BuildRequires:    R-CRAN-vcd 
BuildRequires:    R-grid 
BuildRequires:    R-MASS 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ca 
Requires:         R-CRAN-gnm >= 1.0.3
Requires:         R-CRAN-vcd 
Requires:         R-grid 
Requires:         R-MASS 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-ca 

%description
Provides additional data sets, methods and documentation to complement the
'vcd' package for Visualizing Categorical Data and the 'gnm' package for
Generalized Nonlinear Models. In particular, 'vcdExtra' extends mosaic,
assoc and sieve plots from 'vcd' to handle 'glm()' and 'gnm()' models and
adds a 3D version in 'mosaic3d'.  Additionally, methods are provided for
comparing and visualizing lists of 'glm' and 'loglm' objects. This package
is now a support package for the book, "Discrete Data Analysis with R" by
Michael Friendly and David Meyer.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
