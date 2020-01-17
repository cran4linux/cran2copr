%global packname  HH
%global packver   3.1-39
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.39
Release:          1%{?dist}
Summary:          Statistical Analysis and Data Display: Heiberger and Holland

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-gridExtra >= 2.0
BuildRequires:    R-CRAN-Rmpfr >= 0.6.0
BuildRequires:    R-CRAN-shiny >= 0.13.1
BuildRequires:    R-lattice 
BuildRequires:    R-stats 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-leaps 
BuildRequires:    R-CRAN-vcd 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
Requires:         R-CRAN-gridExtra >= 2.0
Requires:         R-CRAN-Rmpfr >= 0.6.0
Requires:         R-CRAN-shiny >= 0.13.1
Requires:         R-lattice 
Requires:         R-stats 
Requires:         R-grid 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-multcomp 
Requires:         R-graphics 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-leaps 
Requires:         R-CRAN-vcd 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-abind 
Requires:         R-grDevices 
Requires:         R-methods 

%description
Support software for Statistical Analysis and Data Display (Second
Edition, Springer, ISBN 978-1-4939-2121-8, 2015) and (First Edition,
Springer, ISBN 0-387-40270-5, 2004) by Richard M. Heiberger and Burt
Holland.  This contemporary presentation of statistical methods features
extensive use of graphical displays for exploring data and for displaying
the analysis.  The second edition includes redesigned graphics and
additional chapters. The authors emphasize how to construct and interpret
graphs, discuss principles of graphical design, and show how accompanying
traditional tabular results are used to confirm the visual impressions
derived directly from the graphs. Many of the graphical formats are novel
and appear here for the first time in print.  All chapters have exercises.
All functions introduced in the book are in the package.  R code for all
examples, both graphs and tables, in the book is included in the scripts
directory of the package.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/scripts
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
