%global __brp_check_rpaths %{nil}
%global packname  bayesboot
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          3%{?dist}%{?buildtag}
Summary:          An Implementation of Rubin's (1981) Bayesian Bootstrap

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plyr >= 1.8.3
BuildRequires:    R-CRAN-HDInterval >= 0.1.1
Requires:         R-CRAN-plyr >= 1.8.3
Requires:         R-CRAN-HDInterval >= 0.1.1

%description
Functions for performing the Bayesian bootstrap as introduced by Rubin
(1981) <doi:10.1214/aos/1176345338> and for summarizing the result. The
implementation can handle both summary statistics that works on a weighted
version of the data and summary statistics that works on a resampled data
set.

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
