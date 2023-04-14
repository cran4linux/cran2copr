%global __brp_check_rpaths %{nil}
%global packname  mvna
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Nelson-Aalen Estimator of the Cumulative Hazard in MultistateModels

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-lattice 
Requires:         R-lattice 

%description
Computes the Nelson-Aalen estimator of the cumulative transition hazard
for arbitrary Markov multistate models <ISBN:978-0-387-68560-1>.

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
