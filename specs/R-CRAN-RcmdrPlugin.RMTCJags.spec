%global packname  RcmdrPlugin.RMTCJags
%global packver   1.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          2%{?dist}
Summary:          R MTC Jags 'Rcmdr' Plugin

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    xorg-x11-server-Xvfb
BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rcmdr >= 2.0.0
BuildRequires:    R-CRAN-runjags 
BuildRequires:    R-CRAN-rmeta 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-rjags 
Requires:         R-CRAN-Rcmdr >= 2.0.0
Requires:         R-CRAN-runjags 
Requires:         R-CRAN-rmeta 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-rjags 

%description
Mixed Treatment Comparison is a methodology to compare directly and/or
indirectly health strategies (drugs, treatments, devices). This package
provides an 'Rcmdr' plugin to perform Mixed Treatment Comparison for
binary outcome using BUGS code from Bristol University (Lu and Ades).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
xvfb-run %{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

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
%doc %{rlibdir}/%{packname}/CHANGES
%doc %{rlibdir}/%{packname}/etc
%{rlibdir}/%{packname}/INDEX
