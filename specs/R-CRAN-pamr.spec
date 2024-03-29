%global __brp_check_rpaths %{nil}
%global packname  pamr
%global packver   1.56.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.56.1
Release:          3%{?dist}%{?buildtag}
Summary:          Pam: Prediction Analysis for Microarrays

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-cluster 
BuildRequires:    R-survival 
Requires:         R-cluster 
Requires:         R-survival 

%description
Some functions for sample classification in microarrays.

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
