%global packname  rysgran
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}
Summary:          Grain size analysis, textural classifications and distributionof unconsolidated sediments

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-soiltexture 
BuildRequires:    R-lattice 
Requires:         R-CRAN-soiltexture 
Requires:         R-lattice 

%description
This package is a port to R of the SysGran program, written in Delphi by
Camargo (2006). It contains functions for the analysis of grain size
samples (in logarithmic (phi) and geometric (micrometers) scale) based on
various methods, like Folk & Ward (1957) and Methods of Moments (Tanner,
1995), among others; textural classifications and distribution of
unconsolidated sediments are shown in histograms, bivariated plots and
ternary diagrams of Shepard (1954) and Pejrup (1988). English and
Portuguese languages are supported in outputs

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
