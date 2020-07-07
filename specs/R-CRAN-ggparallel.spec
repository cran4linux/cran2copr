%global packname  ggparallel
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}
Summary:          Variations of Parallel Coordinate Plots for Categorical Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-reshape2 >= 1.4.2
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-reshape2 >= 1.4.2

%description
Create hammock plots, parallel sets, and common angle plots with
'ggplot2'.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/adj-angle.pdf
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/new-try.R
%doc %{rlibdir}/%{packname}/references.bib
%{rlibdir}/%{packname}/INDEX
