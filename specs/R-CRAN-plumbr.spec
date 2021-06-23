%global __brp_check_rpaths %{nil}
%global packname  plumbr
%global packver   0.6.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.9
Release:          3%{?dist}%{?buildtag}
Summary:          Mutable and dynamic data models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-objectSignals >= 0.10.2
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-CRAN-objectSignals >= 0.10.2
Requires:         R-utils 
Requires:         R-methods 

%description
The base R data.frame, like any vector, is copied upon modification. This
behavior is at odds with that of GUIs and interactive graphics. To rectify
this, plumbr provides a mutable, dynamic tabular data model. Models may be
chained together to form the complex plumbing necessary for sophisticated
graphical interfaces. Also included is a general framework for linking
datasets; an typical use case would be a linked brush.

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
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
