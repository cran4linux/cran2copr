%global packname  fcm
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          3%{?dist}
Summary:          Inference of Fuzzy Cognitive Maps (FCMs)

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 

%description
Provides a selection of 3 different inference rules (including
additionally the clamped types of the referred inference rules) and 4
threshold functions in order to obtain the inference of the FCM (Fuzzy
Cognitive Map). Moreover, the 'fcm' package returns a data frame of the
concepts' values of each state after the inference procedure. Fuzzy
cognitive maps were introduced by Kosko (1986)
<doi:10.1002/int.4550010405> providing ideal causal cognition tools for
modeling and simulating dynamic systems.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
