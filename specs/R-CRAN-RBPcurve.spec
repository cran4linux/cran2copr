%global __brp_check_rpaths %{nil}
%global packname  RBPcurve
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}%{?buildtag}
Summary:          The Residual-Based Predictiveness Curve

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-mlr >= 2.11
BuildRequires:    R-CRAN-checkmate >= 1.8.2
BuildRequires:    R-CRAN-BBmisc >= 1.11
BuildRequires:    R-CRAN-shape 
BuildRequires:    R-CRAN-TeachingDemos 
Requires:         R-CRAN-mlr >= 2.11
Requires:         R-CRAN-checkmate >= 1.8.2
Requires:         R-CRAN-BBmisc >= 1.11
Requires:         R-CRAN-shape 
Requires:         R-CRAN-TeachingDemos 

%description
The RBP curve is a visual tool to assess the performance of prediction
models.

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
