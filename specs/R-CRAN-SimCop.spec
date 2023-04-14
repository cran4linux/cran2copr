%global __brp_check_rpaths %{nil}
%global packname  SimCop
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          3%{?dist}%{?buildtag}
Summary:          Simulate from Arbitrary Copulae

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-quadprog 
Requires:         R-stats 

%description
Provides a framework to generating random variates from arbitrary
multivariate copulae, while concentrating on (bivariate) extreme value
copulae.  Particularly useful if the multivariate copulae are not
available in closed form.

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
