%global packname  RcmdrPlugin.coin
%global packver   1.0-22
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.22
Release:          3%{?dist}%{?buildtag}
Summary:          Rcmdr Coin Plug-In

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-Rcmdr >= 1.7.0
BuildRequires:    R-CRAN-coin 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-multcomp 
Requires:         R-CRAN-Rcmdr >= 1.7.0
Requires:         R-CRAN-coin 
Requires:         R-survival 
Requires:         R-CRAN-multcomp 

%description
This package provides a Rcmdr "plug-in" based on coin (Conditional
Inference Procedures in a Permutation Test Framework).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/etc
%{rlibdir}/%{packname}/INDEX
