%global packname  Rwofost
%global packver   0.6-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.3
Release:          1%{?dist}
Summary:          WOFOST Crop Growth Simulation Model

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-methods >= 0.2.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.4
BuildRequires:    R-CRAN-meteor 
Requires:         R-methods >= 0.2.2
Requires:         R-CRAN-Rcpp >= 0.12.4
Requires:         R-CRAN-meteor 

%description
An implementation of the WOFOST ("World Food Studies") crop growth model.
WOFOST is a dynamic simulation model that uses daily weather data, and
crop, soil and management parameters to simulate crop growth and
development. See De Wit et al. (2019) <doi:10.1016/j.agsy.2018.06.018> for
a recent review of the history and use of the model.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/wofost
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
