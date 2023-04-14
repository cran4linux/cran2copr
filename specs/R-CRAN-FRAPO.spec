%global __brp_check_rpaths %{nil}
%global packname  FRAPO
%global packver   0.4-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          3%{?dist}%{?buildtag}
Summary:          Financial Risk Modelling and Portfolio Optimisation with R

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.3
Requires:         R-core >= 3.1.3
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-cccp 
BuildRequires:    R-CRAN-Rglpk 
BuildRequires:    R-CRAN-timeSeries 
Requires:         R-methods 
Requires:         R-CRAN-cccp 
Requires:         R-CRAN-Rglpk 
Requires:         R-CRAN-timeSeries 

%description
Accompanying package of the book 'Financial Risk Modelling and Portfolio
Optimisation with R', second edition. The data sets used in the book are
contained in this package.

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
