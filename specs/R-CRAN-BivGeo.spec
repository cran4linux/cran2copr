%global __brp_check_rpaths %{nil}
%global packname  BivGeo
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Basu-Dhar Bivariate Geometric Distribution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Computes the joint probability mass function (pmf), the joint cumulative
function (cdf), the joint survival function (sf), the correlation
coefficient, the covariance, the cross-factorial moment and generate
random deviates for the Basu-Dhar bivariate geometric distribution as well
the joint probability mass, cumulative and survival function assuming the
presence of a cure fraction given by the standard bivariate mixture cure
fraction model. The package also computes the estimators based on the
method of moments.

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
