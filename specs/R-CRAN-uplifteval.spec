%global packname  uplifteval
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Uplift Model Evaluation with Plots and Metrics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-whisker 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-whisker 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-dplyr 

%description
Provides a variety of plots and metrics to evaluate uplift models
including the 'R uplift' package's Qini metric and Qini plot, a port of
the 'python pylift' module's plotting function, and an alternative plot
(in beta) useful for continuous outcomes. Background: Radcliffe (2007)
<https://pdfs.semanticscholar.org/147b/32f3d56566c8654a9999c5477dded233328e.pdf>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
