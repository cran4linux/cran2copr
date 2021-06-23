%global __brp_check_rpaths %{nil}
%global packname  kzfs
%global packver   1.5.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Multi-Scale Motions Separation with Kolmogorov-ZurbenkoPeriodogram Signals

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.2
Requires:         R-core >= 3.3.2
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-kzft 
Requires:         R-methods 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-kzft 

%description
Separation of wave motions in different scales and directions based on
Kolmogorov-Zurbenko Periodograms and Kolmogorov-Zurbenko Fourier
Transform.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
