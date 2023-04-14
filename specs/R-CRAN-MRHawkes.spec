%global __brp_check_rpaths %{nil}
%global packname  MRHawkes
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Multivariate Renewal Hawkes Process

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-IHSEP 
BuildRequires:    R-stats 
Requires:         R-CRAN-IHSEP 
Requires:         R-stats 

%description
Simulate a (bivariate) multivariate renewal Hawkes (MRHawkes)
self-exciting process, with given immigrant hazard rate functions and
offspring density function. Calculate the likelihood of a MRHawkes process
with given hazard rate functions and offspring density function for an
(increasing) sequence of event times. Calculate the Rosenblatt residuals
of the event times. Predict future event times based on observed event
times up to a given time. For details see Stindl and Chen (2018)
<doi:10.1016/j.csda.2018.01.021>.

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
