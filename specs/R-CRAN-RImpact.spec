%global __brp_check_rpaths %{nil}
%global packname  RImpact
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Calculates Measures of Scholarly Impact

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
The metrics() function calculates measures of scholarly impact. These
include conventional measures, such as the number of publications and the
total citations to all publications, as well as modern and robust metrics
based on the vector of citations associated with each publication, such as
the h index and many of its variants or rivals. These methods are
described in Ruscio et al. (2012) <DOI: 10.1080/15366367.2012.711147>.

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
