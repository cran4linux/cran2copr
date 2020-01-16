%global packname  tempR
%global packver   0.9.9.16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.9.16
Release:          1%{?dist}
Summary:          Temporal Sensory Data Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-graphics 

%description
Analysis and visualization of data from temporal sensory methods,
including for temporal check-all-that-apply (TCATA) and temporal dominance
of sensations (TDS).

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
%{rlibdir}/%{packname}/INDEX
