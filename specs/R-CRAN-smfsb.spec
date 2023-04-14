%global __brp_check_rpaths %{nil}
%global packname  smfsb
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Stochastic Modelling for Systems Biology

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.9.0
Requires:         R-core >= 2.9.0
BuildRequires:    R-parallel >= 3.2.0
BuildRequires:    R-CRAN-abind >= 1.3
Requires:         R-parallel >= 3.2.0
Requires:         R-CRAN-abind >= 1.3

%description
Code and data for modelling and simulation of stochastic kinetic
biochemical network models. It contains the code and data associated with
the second and third editions of the book Stochastic Modelling for Systems
Biology, published by Chapman & Hall/CRC Press.

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
