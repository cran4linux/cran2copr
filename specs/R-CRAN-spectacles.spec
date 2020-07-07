%global packname  spectacles
%global packver   0.5-2-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2.2
Release:          3%{?dist}
Summary:          Storing, Manipulating and Analysis Spectroscopy and AssociatedData

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14
Requires:         R-core >= 2.14
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-baseline 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-epiR 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-baseline 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-epiR 

%description
Stores and eases the manipulation of spectra and associated data, with
dedicated classes for spatial and soil-related data.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
