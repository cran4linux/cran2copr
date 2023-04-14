%global __brp_check_rpaths %{nil}
%global packname  eegkit
%global packver   1.0-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Toolkit for Electroencephalography Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-eegkitdata 
BuildRequires:    R-CRAN-bigsplines 
BuildRequires:    R-CRAN-ica 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-signal 
Requires:         R-CRAN-eegkitdata 
Requires:         R-CRAN-bigsplines 
Requires:         R-CRAN-ica 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-signal 

%description
Analysis and visualization tools for electroencephalography (EEG) data.
Includes functions for (i) plotting EEG data, (ii) filtering EEG data,
(iii) smoothing EEG data; (iv) frequency domain (Fourier) analysis of EEG
data, (v) Independent Component Analysis of EEG data, and (vi) simulating
event-related potential EEG data.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
