%global packname  MPV
%global packver   1.55
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.55
Release:          3%{?dist}%{?buildtag}
Summary:          Data Sets from Montgomery, Peck and Vining

License:          Unlimited
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0.1
Requires:         R-core >= 2.0.1
BuildArch:        noarch
BuildRequires:    R-KernSmooth 
Requires:         R-KernSmooth 

%description
Most of this package consists of data sets from the textbook Introduction
to Linear Regression Analysis (3rd ed), by Montgomery, Peck and Vining.
Some additional data sets and functions related to visualization of linear
and nonparametric regression results are included.

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
