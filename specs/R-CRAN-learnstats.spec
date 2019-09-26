%global packname  learnstats
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          An Interactive Environment for Learning Statistics

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-Rcmdr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-Rcmdr 

%description
Allows students to use R as an interactive educational environment for
statistical concepts, ranging from p-values to confidence intervals to
stability in time series.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/betabinomial
%doc %{rlibdir}/%{packname}/fdist
%doc %{rlibdir}/%{packname}/introbinomial
%doc %{rlibdir}/%{packname}/normapprox2bin
%doc %{rlibdir}/%{packname}/propconfint
%doc %{rlibdir}/%{packname}/tdist
%doc %{rlibdir}/%{packname}/timeseries
%doc %{rlibdir}/%{packname}/twonorm
%doc %{rlibdir}/%{packname}/uniform
%{rlibdir}/%{packname}/INDEX
