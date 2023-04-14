%global __brp_check_rpaths %{nil}
%global packname  gvlma
%global packver   1.0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Global Validation of Linear Models Assumptions

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.1.1
Requires:         R-core >= 2.1.1
BuildArch:        noarch

%description
Methods from the paper: Pena, EA and Slate, EH, "Global Validation of
Linear Model Assumptions," J. American Statistical Association,
101(473):341-354, 2006.

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
