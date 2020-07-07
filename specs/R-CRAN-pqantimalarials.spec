%global packname  pqantimalarials
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          3%{?dist}
Summary:          web tool for estimating under-five deaths caused by poor-qualityantimalarials in sub-Saharan Africa

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.1
Requires:         R-core >= 2.14.1
BuildArch:        noarch
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-shiny 

%description
This package allows users to calculate the number of under-five child
deaths caused by consumption of poor quality antimalarials across 39
sub-Saharan nations. The package supports one function, that starts an
interactive web tool created using the shiny R package. The web tool runs
locally on the user's machine. The web tool allows users to set input
parameters (prevalence of poor quality antimalarials, case fatality rate
of children who take poor quality antimalarials, and sample size) which
are then used to perform an uncertainty analysis following the Latin
hypercube sampling scheme. Users can download the output figures as PDFs,
and the output data as CSVs. Users can also download their input
parameters for reference. This package was designed to accompany the
analysis presented in: J. Patrick Renschler, Kelsey Walters, Paul Newton,
Ramanan Laxminarayan "Estimated under-five deaths associated with
poor-quality antimalarials in sub-Saharan Africa", 2014. Paper submitted.

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
%doc %{rlibdir}/%{packname}/tests
%doc %{rlibdir}/%{packname}/webtool
%{rlibdir}/%{packname}/INDEX
