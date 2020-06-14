%global packname  vdg
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          2%{?dist}
Summary:          Variance Dispersion Graphs and Fraction of Design Space Plots

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-parallel 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-proxy 
Requires:         R-splines 
Requires:         R-CRAN-gridExtra 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Facilities for constructing variance dispersion graphs, fraction-
of-design-space plots and similar graphics for exploring the properties of
experimental designs. The design region is explored via random sampling,
which allows for more flexibility than traditional variance dispersion
graphs. A formula interface is leveraged to provide access to complex
model formulae. Graphics can be constructed simultaneously for multiple
experimental designs and/or multiple model formulae. Instead of using
pointwise optimization to find the minimum and maximum scaled prediction
variance curves, which can be inaccurate and time consuming, this package
uses quantile regression as an alternative.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
