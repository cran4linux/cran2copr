%global packname  patternplot
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Versatile Pie Charts, Ring Charts, Bar Charts and Box Plotsusing Patterns, Colors and Images

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-R6 >= 2.1.2
BuildRequires:    R-CRAN-ggplot2 >= 2.1.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-jpeg >= 0.1.8
BuildRequires:    R-CRAN-png >= 0.1.7
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-CRAN-R6 >= 2.1.2
Requires:         R-CRAN-ggplot2 >= 2.1.0
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-jpeg >= 0.1.8
Requires:         R-CRAN-png >= 0.1.7
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-gridExtra 

%description
Creates aesthetically pleasing and informative pie charts, ring charts,
bar charts and box plots with colors, patterns, and images.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/img
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
