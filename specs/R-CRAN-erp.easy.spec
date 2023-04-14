%global __brp_check_rpaths %{nil}
%global packname  erp.easy
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Event-Related Potential (ERP) Data Exploration Made Easy

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gtools >= 3.5.0
BuildRequires:    R-CRAN-plyr >= 1.8.3
BuildRequires:    R-CRAN-signal >= 0.7.6
Requires:         R-CRAN-gtools >= 3.5.0
Requires:         R-CRAN-plyr >= 1.8.3
Requires:         R-CRAN-signal >= 0.7.6

%description
A set of user-friendly functions to aid in organizing, plotting and
analyzing event-related potential (ERP) data.  Provides an easy-to-learn
method to explore ERP data. Should be useful to those without a background
in computer programming, and to those who are new to ERPs (or new to the
more advanced ERP software available). Emphasis has been placed on highly
automated processes using functions with as few arguments as possible.
Expects processed (cleaned) data.

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
