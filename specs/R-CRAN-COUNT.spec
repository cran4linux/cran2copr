%global __brp_check_rpaths %{nil}
%global packname  COUNT
%global packver   1.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.4
Release:          3%{?dist}%{?buildtag}
Summary:          Functions, Data and Code for Count Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-msme 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-MASS 
Requires:         R-CRAN-msme 
Requires:         R-CRAN-sandwich 
Requires:         R-MASS 

%description
Functions, data and code for Hilbe, J.M. 2011. Negative Binomial
Regression, 2nd Edition (Cambridge University Press) and Hilbe, J.M. 2014.
Modeling Count Data (Cambridge University Press).

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
